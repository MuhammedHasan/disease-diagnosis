import requests
import json
from collections import Counter

from sklearn.base import TransformerMixin
from sklearn.feature_extraction import DictVectorizer


class MetabolicSolutionScaler(TransformerMixin):
    """Scaler for converting change level data to pathway level"""

    def __init__(self, vectorizer: DictVectorizer):
        self.vectorizer = vectorizer
        self.url = 'http://metabolitics.biodb.sehir.edu.tr/api3/'

    def fit(self, X, y):
        return self

    def transform(self, X, y):
        pass

    def _get_key(self, data):
        ''' Start analysis and get key of result '''
        req = requests.post('%ssubsystems-analyze-start' % self.url,
                            data=json.dumps(data),
                            headers={'content-type': 'application/json'})
        return json.loads(req.text)

    def _get_solution_data(self, key):
        ''' Get output data of analysis '''
        req = requests.get('%ssubsystems-analyze/%s' % (self.url, key))
        return json.loads(req.text)

    def to_ecoli(self, X):
        ''' Convert metabolite names to ecolin database ids '''
        X = self.vectorizer.inverse_transform(X)

    def _get_solution(self, metabolite_contration):
        data = {
            'name': 'my anaylsis',
            'concentrationChanges': [
                {'name': k, 'change': v}
                for k, v in metabolite_contration.items()
            ]
        }
        return self._get_solution_data(self._get_key(data))

    def _pathway_activation_score(self, solutions):
        ''' Score subsystems by how many time it is repated in solutions '''
        return [dict(Counter([x for i in s.values() for x in i]))
                for s in solutions]

    def get_solutions(self, metabolite_contrations):
        ''' Score subsystems by how many time it is repated in solutions '''
        return [self._get_solution(i) for i in metabolite_contrations]

    def fit_transform(self, X, y):
        return self.fit(X, y).transform(X, y)
