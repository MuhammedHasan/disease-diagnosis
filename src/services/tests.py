import unittest
import logging

from .solution_service import SolutionService
from .naming_service import NamingService
from .data_reader import DataReader


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


class TestNamingService(unittest.TestCase):

    def setUp(self):
        self.service = NamingService('ecolin')

    def test_to(self):
        self.assertNotEqual(len(self.service._names), 0)

        self.service._names = {'x': 'y'}
        self.assertEqual(self.service.to('x'), 'y')
        self.assertEqual(self.service.to('a'), None)

        named = self.service.to({'x': 1, 'c': 1})
        self.assertDictEqual(named, {'y': 1})


class TestDataReader(unittest.TestCase):

    def setUp(self):
        self.service = DataReader()

    def test_solution_reader(self):
        self.assertNotEqual(len(self.service.read_solutions()), 0)
