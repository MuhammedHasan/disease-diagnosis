from preprocessing.tests import TestMetabolicStandardScaler
from preprocessing.tests import TestMetabolicChangeScaler
from preprocessing.tests import TestMetabolicSolutionScaler
from preprocessing.tests import TestMostActivePathwayScaler


from classifiers.tests import TestMetaboliteLevelDiseaseClassifier
from classifiers.tests import TestSolutionLevelDiseaseClassifier
from classifiers.tests import TestFromSolutionSolutionLevelDiseaseClassifier
from classifiers.tests import TestDummyClassifier

from services.tests import TestSolutionService
from services.tests import TestNamingService
from services.tests import TestDataReader

import unittest

if __name__ == "__main__":
    unittest.main()
