import unittest
from utilities import calculate_standard_deviation

class TestStandardDeviation(unittest.TestCase):
    def test_integer_standard_deviation(self):
        self.assertAlmostEqual(calculate_standard_deviation([1, 2, 3, 4, 5]), 1.4142, places=4)

    def test_identical_values(self):
        self.assertEqual(calculate_standard_deviation([5, 5, 5]), 0)

    def test_single_value(self):
        self.assertEqual(calculate_standard_deviation([10]), 0)

    def test_floating_point_standard_deviation(self):
        self.assertAlmostEqual(calculate_standard_deviation([1.1, 2.2, 3.3, 4.4, 5.5]), 1.5556, places=4)

    def test_negative_numbers(self):
        self.assertAlmostEqual(calculate_standard_deviation([-5, -4, -3, -2, -1]), 1.4142, places=4)

    def test_mixed_positive_and_negative(self):
        self.assertAlmostEqual(calculate_standard_deviation([-3, -2, 0, 2, 3]), 2.2803508501983, places=4)

    def test_large_numbers(self):
        self.assertAlmostEqual(calculate_standard_deviation([1_000_000, 1_000_001, 1_000_002, 1_000_003, 1_000_004]), 1.4142, places=4)
    
    def test_small_numbers(self):
        self.assertAlmostEqual(calculate_standard_deviation([0.001, 0.002, 0.003, 0.004, 0.005]), 0.0014, places=4)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_standard_deviation([])

    def test_outlier(self):
        self.assertEqual(calculate_standard_deviation([5, 5, 5, 5, 100]), 38)