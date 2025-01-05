import unittest
from src.utilities import calculate_loan_to_value

class TestLoanToValue(unittest.TestCase):
    def test_loan_to_value_basic(self):
        loan_to_value = calculate_loan_to_value(loan_amount=40000, property_value=100000)
        self.assertEqual(loan_to_value, 40)

    def test_loan_to_value_full(self):
        loan_to_value = calculate_loan_to_value(loan_amount=100000, property_value=100000)
        self.assertEqual(loan_to_value, 100)

    def test_zero_loan(self):
        loan_to_value = calculate_loan_to_value(loan_amount=0, property_value=100000)
        self.assertEqual(loan_to_value, 0)

    def test_floating_point_values(self):
        loan_to_value = calculate_loan_to_value(loan_amount=40000.5, property_value=100000.4)
        self.assertAlmostEqual(loan_to_value, 40, places=3)

    def test_loan_greater_than_property_value(self):
        loan_to_value = calculate_loan_to_value(loan_amount=150000, property_value=100000)
        self.assertEqual(loan_to_value, 150)

    def test_negative_property_value(self):
        with self.assertRaises(ValueError):
            calculate_loan_to_value(loan_amount=150000, property_value=-100000)

    def test_zero_property_value(self):
        with self.assertRaises(ValueError):
            calculate_loan_to_value(loan_amount=150000, property_value=0)

    def test_negative_loan(self):
        with self.assertRaises(ValueError):
            calculate_loan_to_value(loan_amount=-50000, property_value=100000)