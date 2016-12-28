from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer

from .base_disease_clustering import BaseDiseaseClustering
from preprocessing import MostActivePathwayScaler


class MetaboliteLevelDiseaseClustering(BaseDiseaseClustering):

    def __init__(self):
        super().__init__()
        self._pipe = Pipeline([
            ('scaler_most_active', MostActivePathwayScaler()),
            ('vect', DictVectorizer(sparse=False)),
            ('pca', PCA()),
            ('clf', AgglomerativeClustering(n_clusters=3,
                                            affinity="manhattan",
                                            linkage="complete"))
        ])
