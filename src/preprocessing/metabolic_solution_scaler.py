import json
from collections import Counter

from sklearn.base import TransformerMixin
from sklearn.feature_extraction import DictVectorizer

from services import SolutionService


class MetabolicSolutionScaler(TransformerMixin):
    """Scaler for converting change level data to pathway level"""

    def __init__(self, vectorizer: DictVectorizer):
        self.vectorizer = vectorizer
        self.solution_service = SolutionService()
        self.ecolin_vectorizer = DictVectorizer(sparse=False)
        self.url = 'http://metabolitics.biodb.sehir.edu.tr/api3/'

    def fit(self, X, y):
        ecolin_X = self.to_ecolin(X)
        solutions = self.solution_service.get_solutions(ecolin_X)
        solutions_scores = self._pathway_activation_score(solutions)
        self.ecolin_vectorizer.fit(solutions_scores, y)
        return self

    def transform(self, X, y=[]):
        ecolin_X = self.to_ecolin(X)
        solutions = self.solution_service.get_solutions(ecolin_X)
        solutions_scores = self._pathway_activation_score(solutions)
        return self.ecolin_vectorizer.transform(solutions_scores)

    def fit_transform(self, X, y):
        return self.fit(X, y).transform(X, y)

    def to_ecolin(self, X):
        ''' Convert metabolite names to ecolin database ids '''
        X = self.vectorizer.inverse_transform(X)
        with open('../dataset/naming/ecolin-mapping.json') as f:
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
