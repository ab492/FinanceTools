import unittest
from utilities import calculate_loan_to_value

class TestLoanToValue(unittest.TestCase):
    def test_loan_to_value_basic(self):
        loan_to_value = calculate_loan_to_value(loan_amount=40000, property_value=100000)
        self.assertEqual(loan_to_value, 40)

    def test_loan_to_value_full(self):
        loan_to_value = calculate_loan_to_value(loan_amount=100000, property_value=100000)
        self.assertEqual(loan_to_value, 100)


