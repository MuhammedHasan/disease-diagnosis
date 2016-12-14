import os

import pandas as pd

from sklearn.metrics import classification_report


class BaseDiseaseClassifier(object):

    def __init__(self):
        self.y_label = 'stage'
        self._model = object()
        self.path = '../dataset/disease'

    def read_data(self, disease_name):
        df_bc = pd.read_csv('%s/%s.csv' % (self.path, disease_name), header=0)
        X = df_bc.ix[:, df_bc.columns != self.y_label].to_dict('records')
        y = df_bc[self.y_label].values
        y = ['h' if i == 'h' else disease_name.lower() for i in y]
        return (X, y)

    def read_all(self):
        disease_names = [f[:-4] for f in os.listdir(self.path)]
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
