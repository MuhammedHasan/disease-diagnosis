from sklearn.metrics import classification_report, accuracy_score


class BaseDiseaseClustering(object):

    def __init__(self):
        self._model = object()

    def fit(self, X, y):
        self._model = self._pipe.fit(X, y)

    def fit_predict(self, X, y):
        '''
        Fits and return class labels
        '''
        prediction = self._pipe.fit_predict(X, y)

        for i in prediction:
            if i == 1:
                yield 'h'
            elif i == 0:
                yield 'hcc'
            elif i == 2:
                yield 'bc'

    def score(self, X, y):
        '''
        Score of model
        '''
        return accuracy_score([i for i in self.fit_predict(X, y)], y)

    def classification_report(self, X, y):
        '''
        '''
        return classification_report(y, [i for i in self.fit_predict(X, y)])

    def __str__(self):
        return str(self._model)
