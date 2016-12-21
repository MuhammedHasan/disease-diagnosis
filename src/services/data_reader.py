import os

import pandas as pd


class DataReader(object):

    def __init__(self):
        self.path = '../dataset/disease'
        self.y_label = 'stage'

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

    def read_avg_data(self):
        raise NotImplementedError()

    def read_small_data(self):
        self.path = '../dataset/small-disease'
        return self.read_all()
