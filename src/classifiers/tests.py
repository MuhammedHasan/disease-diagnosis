import unittest
import logging

from .metabolite_level_disease_classifier \
    import MetaboliteLevelDiseaseClassifier
from .solution_level_disease_classifier import SolutionLevelDiseaseClassifier

from sklearn.model_selection import train_test_split

LOG_FILENAME = '../logs/classification.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)


class TestMetaboliteLevelDiseaseClassifier(unittest.TestCase):

    def setUp(self):
        self.clf = MetaboliteLevelDiseaseClassifier()
        (X, y) = self.clf.read_all()

        (self.X_train, self.X_test, self.y_train, self.y_test) =  \
            train_test_split(X, y, random_state=0)

        self.clf.fit(self.X_train, self.y_train)

    def test_accuracy(self):
        logging.info('\n %s \n' % str(self.clf))

        train_accuracy = self.clf.score(self.X_train, self.y_train)
        logging.info('train accuracy: %f' % train_accuracy)

        test_accuracy = self.clf.score(self.X_test, self.y_test)
        logging.info('test accuracy: %f' % test_accuracy)

    def test_classification_report(self):
        cr = self.clf.classification_report(self.X_test, self.y_test)
        logging.info('\n %s' % cr)


class TestSolutionLevelDiseaseClassifier(unittest.TestCase):

    def setUp(self):
        self.clf = SolutionLevelDiseaseClassifier()
        (X, y) = self.clf.read_all()

        (self.X_train, self.X_test, self.y_train, self.y_test) =  \
            train_test_split(X, y, random_state=0)

        self.clf.fit(self.X_train, self.y_train)

    def test_accuracy(self):
        logging.info('\n %s \n' % str(self.clf))

        train_accuracy = self.clf.score(self.X_train, self.y_train)
        logging.info('train accuracy: %f' % train_accuracy)

        test_accuracy = self.clf.score(self.X_test, self.y_test)
        logging.info('test accuracy: %f' % test_accuracy)

    def test_classification_report(self):
        cr = self.clf.classification_report(self.X_test, self.y_test)
        logging.info('\n %s' % cr)
