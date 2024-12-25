import unittest
from utilities import calculate_mean

class TestMean(unittest.TestCase):
    def test_single_value(self):
        self.assertEqual(calculate_mean([10]), 10)

    def test_multiple_values_with_int_mean(self):
        self.assertEqual(calculate_mean([10, 12]), 11)