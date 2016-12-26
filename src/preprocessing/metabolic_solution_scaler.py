
from sklearn.base import TransformerMixin
from sklearn.feature_extraction import DictVectorizer

from services import SolutionService, NamingService


class MetabolicSolutionScaler(TransformerMixin):
    """Scaler for converting change level data to pathway level"""

    def __init__(self, vectorizer: DictVectorizer):
        self.vectorizer = vectorizer
        self.solution_service = SolutionService()
        self.naming = NamingService('ecolin')

    def fit(self, X, y):
        return self

    def transform(self, X, y=[]):
        ecolin_X = self.naming.to(X)
        solutions = self.solution_service.get_solutions(ecolin_X)
        return solutions

    def fit_transform(self, X, y):
        return self.fit(X, y).transform(X, y)
