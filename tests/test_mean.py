import unittest
from utilities import calculate_mean

class TestMean(unittest.TestCase):
    def test_single_value(self):
        self.assertEqual(calculate_mean([10]), 10)
