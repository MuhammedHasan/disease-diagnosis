from sklearn.feature_extraction import DictVectorizer

from classifiers import BaseDiseaseClassifier
from preprocessing import MetabolicSolutionScaler

bd = BaseDiseaseClassifier()
(X, y) = bd.read_all()

vict = DictVectorizer(sparse=False)
trans_X = vict.fit_transform(X)

mss = MetabolicSolutionScaler(vict)
a = mss.to_ecoli(trans_X)
print(a)
