import unittest
from .metabolic_standard_scaler import MetabolicStandardScaler


class TestMetabolicStandardScaler(unittest.TestCase):

    def setUp(self):
        self.scaler = MetabolicStandardScaler()
        self.X = [[10], [10], [10], [0], [0], [0]]
        self.y = ['bc', 'bc', 'bc', 'h', 'h', 'h']

    def test_partial_fit(self):
        self.scaler.partial_fit(self.X, self.y)
        expected_X = self.X
        transformed_X = self.scaler.transform(self.X, self.y).tolist()
        self.assertEqual(expected_X, transformed_X)
