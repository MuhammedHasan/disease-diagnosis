import unittest

from .extanded_jaccard import extanded_jaccard


class TestExtendedJaccard(unittest.TestCase):

    def setUp(self):
        self.solution_matrix_1 = [['a', 'b', 'c', 'd'],
                                  ['a', 'b', 'c'],
                                  ['a', 'd'],
                                  ['a', 'b', 'd'],
                                  ['d']]

        self.solution_matrix_2 = [['a', 'b', 'c', 'd'],
                                  ['a', 'b'],
                                  ['a', 'b', 'c'],
                                  ['b', 'c'],
                                  ['c']]

    def test_extened_jaccard(self):
        matrix = extanded_jaccard(self.solution_matrix_1,
                                  self.solution_matrix_2)
        self.assertListEqual(sorted(matrix), sorted(['a', 'b', 'd']))
