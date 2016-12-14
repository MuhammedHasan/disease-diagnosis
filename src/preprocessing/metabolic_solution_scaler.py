import requests
import json

from sklearn.base import TransformerMixin


class MetabolicSolutionScaler(TransformerMixin):
    """Scaler for converting change level data to pathway level"""

    def __init__(self, vectorizer):
        self.vectorizer = vectorizer
        self.url = 'http://metabolitics.biodb.sehir.edu.tr/api3/'

    def fit(self, X, y):
        return self

    def transform(self, X, y):
        pass

    def _get_key(self, data):
        req = requests.post('%ssubsystems-analyze-start' % self.url,
                            data=json.dumps(data),
                            headers={'content-type': 'application/json'})
        return json.loads(req.text)

    def _get_solution_data(self, key):
        req = requests.get('%ssubsystems-analyze/%s' % (self.url, key))
        return json.loads(req.text)

    def to_ecoli(self, metabolite_names):
        ''' Convert metabolite names to ecolin database ids '''
        pass

    def _get_solution(self, metabolite_contration):
        data = {
            'name': 'my anaylsis',
            'concentrationChanges': [
                {'name': k, 'change': v}
                for k, v in metabolite_contration.items()
            ]
        }
        return self._get_solution_data(self._get_key(data))

    def get_solutions(self, metabolite_contrations):
        return [self._get_solution(i) for i in metabolite_contrations]

    def fit_transform(self, X, y):
        return self.fit(X, y).transform(X, y)

if __name__ == '__main__':
    mss = MetabolicSolutionScaler(object())
    mss.transform([], [])
