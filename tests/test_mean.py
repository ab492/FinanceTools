import unittest
from utilities import calculate_mean

class TestMean(unittest.TestCase):
    def test_single_value(self):
        self.assertEqual(calculate_mean([10]), 10)

    def test_integer_mean(self):
        self.assertEqual(calculate_mean([10, 12]), 11)

    def test_floating_point_mean(self):
        self.assertEqual(calculate_mean([1.5, 2.5, 3.5]), 2.5)

    def test_mixed_int_and_float_mean(self):
        self.assertAlmostEqual(calculate_mean([1, 2.5, 3]), 2.1667, places=4)
    
    def test_negative_numbers(self):
        self.assertEqual(calculate_mean([-10, -20, -30]), -20)
    
    def test_mixed_positive_and_negative(self):
        self.assertEqual(calculate_mean([-10, 10]), 0)

    def test_large_numbers(self): # Ensure there are no overflow issues
        self.assertEqual(calculate_mean([1_000_000, 2_000_000, 3_000_000]), 2_000_000)
    
    def test_single_floating_point_value(self):
        self.assertEqual(calculate_mean([5.5]), 5.5)