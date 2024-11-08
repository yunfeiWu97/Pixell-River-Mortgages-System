"""
Description: A class used to test the Mortgage class.
Author: Yunfei Wu
Date: 2024-11-08
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    """Unit tests for the Mortgage class."""

    def test_invalid_amount_raises_value_error(self):
        """Test that __init__ raises ValueError for an invalid loan amount."""
        with self.assertRaises(ValueError) as context:
            Mortgage(0, "FIXED_5", "MONTHLY", 25)
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_invalid_rate_raises_value_error(self):
        """Test that __init__ raises ValueError for an invalid rate."""
        with self.assertRaises(ValueError) as context:
            Mortgage(100000, "INVALID_RATE", "MONTHLY", 25)
        self.assertEqual(str(context.exception), "Rate provided is invalid.")

    def test_invalid_frequency_raises_value_error(self):
        """Test that __init__ raises ValueError for an invalid frequency."""
        with self.assertRaises(ValueError) as context:
            Mortgage(100000, "FIXED_5", "INVALID_FREQUENCY", 25)
        self.assertEqual(str(context.exception), "Frequency provided is invalid.")

    def test_invalid_amortization_raises_value_error(self):
        """Test that __init__ raises ValueError for an invalid amortization."""
        with self.assertRaises(ValueError) as context:
            Mortgage(100000, "FIXED_5", "MONTHLY", 35)
        self.assertEqual(str(context.exception), "Amortization provided is invalid.")

    def test_valid_inputs_set_attributes_correctly(self):
        """Test that __init__ sets attributes correctly for valid inputs."""
        mortgage = Mortgage(100000, "FIXED_5", "MONTHLY", 25)
        self.assertEqual(mortgage._Mortgage__loan_amount, 100000)
        self.assertEqual(mortgage._Mortgage__rate, MortgageRate.FIXED_5)
        self.assertEqual(mortgage._Mortgage__frequency, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage._Mortgage__amortization, 25)

    def test_loan_amount_mutator_negative_value(self):
        """Test setting a negative value for loan amount raises ValueError."""
        mortgage = Mortgage(100000, "FIXED_5", "MONTHLY", 25)
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = -50000
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_loan_amount_mutator_zero_value(self):
        """Test setting a zero value for loan amount raises ValueError."""
        mortgage = Mortgage(100000, "FIXED_5", "MONTHLY", 25)
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = 0
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_loan_amount_mutator_positive_value(self):
        """Test setting a positive value for loan amount works correctly."""
        mortgage = Mortgage(100000, "FIXED_5", "MONTHLY", 25)
        mortgage.loan_amount = 150000
        self.assertEqual(mortgage.loan_amount, 150000)

    def test_rate_mutator_valid_enum_value(self):
        """Test setting a valid MortgageRate enum value for rate."""
        mortgage = Mortgage(100000, "FIXED_5", "MONTHLY", 25)
        mortgage.rate = "FIXED_3"
        self.assertEqual(mortgage.rate, MortgageRate.FIXED_3)

    def test_rate_mutator_invalid_value(self):
        """Test setting an invalid value for rate raises ValueError."""
        mortgage = Mortgage(100000, "FIXED_5", "MONTHLY", 25)
        with self.assertRaises(ValueError) as context:
            mortgage.rate = "INVALID_RATE"
        self.assertEqual(str(context.exception), "Rate provided is invalid.")