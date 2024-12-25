import unittest
from utilities import calculate_standard_deviation

class TestStandardDeviation(unittest.TestCase):
    # def test_standard_deviation(self):
    #     self.assertAlmostEqual(calculate_standard_deviation([1, 2, 3, 4, 5]), 1.5811, places=4)

    def test_identical_values(self):
        self.assertEqual(calculate_standard_deviation([5, 5, 5]), 0)

    def test_single_value(self):
        self.assertEqual(calculate_standard_deviation([10]), 0)
