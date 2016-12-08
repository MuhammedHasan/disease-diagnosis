import pandas as pd

from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

from preprocessing.metabolic_standard_scaler import MetabolicStandardScaler


class DiseaseClassifier(object):

    def __init__(self):
        self.y_label = 'Stage of disease'
        self._model = object()
        self._pipe = Pipeline([
            ('scaler', MetabolicStandardScaler()),
            ('pca', PCA()),
            ('clf', SVC(C=0.01, kernel='linear', random_state=5))
        ])

    def read_data(self):
        df_bc = pd.read_csv('../dataset/BC.csv', header=0)
        X = df_bc.ix[:, df_bc.columns != 'Stage of disease'].values
        y = df_bc[self.y_label].values
        y = ['h' if i == 0 else 'bc' for i in y]
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
