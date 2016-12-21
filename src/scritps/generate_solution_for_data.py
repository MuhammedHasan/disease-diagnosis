import json

from sklearn.feature_extraction import DictVectorizer

from preprocessing import MetabolicChangeScaler, MetabolicSolutionScaler
from services import DataReader, SolutionService


def solution_for_dataset():
    (X, y) = DataReader().read_all()

    vect = DictVectorizer(sparse=False)
    X = vect.fit_transform(X, y)
    X = MetabolicChangeScaler().fit_transform(X, y)
    X = MetabolicSolutionScaler(vect).to_ecolin(X)

    solution_service = SolutionService()
    file_path = '../output/solution_for_dataset.json'
    calculated_samples = sum(1 for line in open(file_path))

    f = open(file_path, 'a')
    for x in X[calculated_samples:]:
        solution = solution_service.get_solution(x)
        f.write('%s\n' % json.dumps(solution))
