import json
from collections import Counter

import requests

from sklearn.base import TransformerMixin
from sklearn.feature_extraction import DictVectorizer


class MetabolicSolutionScaler(TransformerMixin):
    """Scaler for converting change level data to pathway level"""

    def __init__(self, vectorizer: DictVectorizer):
        self.vectorizer = vectorizer
        self.ecolin_vectorizer = DictVectorizer(sparse=False)
        self.url = 'http://metabolitics.biodb.sehir.edu.tr/api3/'

    def fit(self, X, y):
        ecolin_X = self.to_ecolin(X)
        solutions = self.get_solutions(ecolin_X)
        solutions_scores = self._pathway_activation_score(solutions)
        self.ecolin_vectorizer.fit(solutions_scores, y)
        return self

    def transform(self, X, y=[]):
        ecolin_X = self.to_ecolin(X)
        solutions = self.get_solutions(ecolin_X)
        solutions_scores = self._pathway_activation_score(solutions)
        return self.ecolin_vectorizer.transform(solutions_scores)

    def fit_transform(self, X, y):
        return self.fit(X, y).transform(X, y)

    def get_solutions(self, metabolite_changes):
        ''' Score subsystems by how many time it is repated in solutions '''
        solutions = [self._get_solution(i) for i in metabolite_changes]
        return solutions

    def _get_solution(self, metabolite_change):
        data = {
            'name': 'my anaylsis',
            'concentrationChanges': [
                {'name': k, 'change': v}
                for k, v in metabolite_change.items()
            ]
        }

        req = requests.post('%ssubsystems-analyze-start' % self.url,
                            data=json.dumps(data),
                            headers={'content-type': 'application/json'})
        key = json.loads(req.text)

        req = requests.get('%ssubsystems-analyze/%s' % (self.url, key))
        output_data = json.loads(req.text)

        return output_data

    def to_ecolin(self, X):
        ''' Convert metabolite names to ecolin database ids '''
        X = self.vectorizer.inverse_transform(X)
        with open('../dataset/ecolin-mapping.json') as f:
            ecolin_mapping = json.load(f)
            return [
                {ecolin_mapping[k]:v for k, v in x.items()
                 if k in ecolin_mapping and ecolin_mapping[k] != ''}
                for x in X
            ]

    def _pathway_activation_score(self, solutions):
        ''' Score subsystems by how many time it is repated in solutions '''
        return [dict(Counter([x for i in s.values() for x in i]))
                for s in solutions]
