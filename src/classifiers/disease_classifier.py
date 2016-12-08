import pandas as pd
import numpy as np

from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.feature_extraction import DictVectorizer

from preprocessing.metabolic_standard_scaler import MetabolicStandardScaler


class DiseaseClassifier(object):

    def __init__(self):
        self.y_label = 'stage'
        self._model = object()
        self._pipe = Pipeline([
            ('vect', DictVectorizer(sparse=False)),
            ('scaler', MetabolicStandardScaler()),
            ('pca', PCA()),
            ('clf', SVC(C=0.01, kernel='rbf', random_state=0))
        ])

    def read_data(self, disease_name):
        df_bc = pd.read_csv('../dataset/%s.csv' % disease_name, header=0)
        X = df_bc.ix[:, df_bc.columns != self.y_label].to_dict('records')
        y = df_bc[self.y_label].values
        y = ['h' if i == 'h' else disease_name.lower() for i in y]
        return (X, y)

    def read_all(self):
        disease_names = ['BC', 'HCC']
        (X, y) = (list(), list())
        for i in disease_names:
            (tX, ty) = self.read_data(i)
            X += tX
            y += ty
        return (X, y)

    def fit(self, X, y):
        '''
        Fits model
        '''
        self._model = self._pipe.fit(X, y)

    def score(self, X, y):
        '''
        Score of model
        '''
        return self._model.score(X, y)

    def predict(self, X):
        '''
        Predicts star for given review and return star
        review: Review object
        '''
        return self._model.predict(X)

    def classification_report(self, X, y):
        '''
        '''
        return classification_report(y, self._model.predict(X))

    def __str__(self):
        return str(self._model)
