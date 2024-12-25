import unittest
from utilities import calculate_standard_deviation

class TestStandardDeviation(unittest.TestCase):
    def test_identical_values(self):
        self.assertEqual(calculate_standard_deviation([5, 5, 5]), 0)

    def test_single_value(self):
        self.assertEqual(calculate_standard_deviation([10]), 0)
