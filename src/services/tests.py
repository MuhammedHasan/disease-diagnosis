import unittest
import logging

from .solution_service import SolutionService


class TestSolutionService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger('services')
        cls.logger.setLevel(logging.INFO)
        cls.logger.addHandler(logging.FileHandler('../logs/services.log'))

    def setUp(self):
        self.data = [{'acon_C_c': 1}, ]
        self.service = SolutionService()

    @unittest.skip('too long tests')
    def test_get_solutions(self):
        solutions = self.service.get_solutions(self.data)
        self.assertNotEqual(len(solutions), 0)
        self.assertNotEqual(len(solutions[0]), 0)
        self.assertNotEqual(len(next(iter(solutions[0].values()))), 0)
