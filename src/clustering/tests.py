import unittest
import logging

from services import DataReader
from .solution_level_clustering import MetaboliteLevelDiseaseClustering

classification_logger = logging.getLogger('clustering')
classification_logger.setLevel(logging.INFO)
classification_logger.addHandler(
    logging.FileHandler('../logs/clustering.log'))


class TestMetaboliteLevelDiseaseClustering(unittest.TestCase):

    def setUp(self):
        self.clf = MetaboliteLevelDiseaseClustering()
        (self.X, self.y) = DataReader().read_solutions()

    def test_accuracy(self):
        classification_logger.info('\n %s \n' % str(self.clf))

        train_accuracy = self.clf.score(self.X, self.y)
        classification_logger.info('train accuracy: %f' % train_accuracy)

    def test_classification_report(self):
        cr = self.clf.classification_report(self.X, self.y)
        classification_logger.info('\n %s' % cr)
