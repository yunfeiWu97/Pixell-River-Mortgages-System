"""
Description: A class used to test the Mortgage class.
Author: Yunfei Wu
Date: 2024-11-08
Usage: Use the tests encapsulated within this class to test the 
       MortgagePayment class.
"""
import unittest
from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    """
    Test cases for the Mortgage class, including validation of loan 
    amount, rate, frequency, amortization, and accessor and mutator functions.
    """

    def test_invalid_loan_amount(self):
        """
        Test that initializing the Mortgage with an invalid loan amount 
        (negative value) raises a ValueError.
        """
        # Arrange
        negative_value = -1000

        # Act  
        with self.assertRaises(ValueError) as context:
            mortgage = Mortgage(negative_value, 'FIXED_5', 'MONTHLY', 20)

        # Assert
        expected = "Loan Amount must be positive."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_invalid_rate(self):
        """
        Test that initializing the Mortgage with an invalid rate 
        (not in MortgageRate enum) raises a ValueError.
        """
        # Arrange
        invalid_rate = 'FIXED_6'

        # Act  
        with self.assertRaises(ValueError) as context:
            mortgage = Mortgage(100000, invalid_rate, 'MONTHLY', 20)

        # Assert
        expected = "Rate provided is invalid."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_invalid_frequency(self):
        """
        Test that initializing the Mortgage with an invalid frequency 
        (not in PaymentFrequency enum) raises a ValueError.
        """
        # Arrange
        invalid_frequency = 'QUARTERLY'

        # Act  
        with self.assertRaises(ValueError) as context:
            mortgage = Mortgage(100000, 'FIXED_5', invalid_frequency, 20)

        # Assert
        expected = "Frequency provided is invalid."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_invalid_amortization(self):
        """
        Test that initializing the Mortgage with an invalid amortization 
        period (not in VALID_AMORTIZATION list) raises a ValueError.
        """
        # Arrange
        invalid_amortization = 40

        # Act  
        with self.assertRaises(ValueError) as context:
            mortgage = Mortgage(
                100000, 'FIXED_5', 'MONTHLY', invalid_amortization
            )
        # Assert
        expected = "Amortization provided is invalid."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_valid_inputs(self):
        """
        Test that initializing the Mortgage with valid inputs correctly 
        sets loan amount, rate, frequency, and amortization attributes.
        """
        # Arrange
        loan_amount = 100000
        rate = 'FIXED_5'
        frequency = 'MONTHLY'
        amortization = 20

        # Act
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)

        # Assert
        self.assertEqual(mortgage._Mortgage__loan_amount, loan_amount)
        self.assertEqual(mortgage._Mortgage__rate, MortgageRate['FIXED_5'])
        self.assertEqual(
            mortgage._Mortgage__frequency, 
            PaymentFrequency['MONTHLY']
        )        
        self.assertEqual(mortgage._Mortgage__amortization, amortization)

    def test_set_negative_loan_amount(self):
        """
        Test the loan_amount mutator: Attempting to set a negative loan 
        amount should raise a ValueError.
        """
        # Arrange
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)

        # Act
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = -50000

        # Assert
        expected = "Loan Amount must be positive."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_set_zero_loan_amount(self):
        """
        Test the loan_amount mutator: Attempting to set a loan amount of
        zero should raise a ValueError.
        """
        # Arrange
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)

        # Act
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = 0

        # Assert
        expected = "Loan Amount must be positive."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_set_positive_loan_amount(self):
        """
        Test the loan_amount mutator: Setting a positive loan amount 
        should correctly update the loan amount attribute.
        """
        # Arrange
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)

        # Act
        mortgage.loan_amount = 150000

        # Assert
        self.assertEqual(mortgage.loan_amount, 150000)

    def test_modify_rate_to_valid(self):
        """
        Test the mutator for rate: Modify the rate to a valid value and 
        verify the result.
        """
        # Arrange
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)

        # Act
        mortgage.rate = 'VARIABLE_1'

        # Assert
        self.assertEqual(mortgage.rate, MortgageRate['VARIABLE_1'])
    
    def test_modify_rate_to_invalid(self):
        """
        Test the mutator for rate: Modify the rate to an invalid value 
        and verify that ValueError is raised.
        """
        # Arrange
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)

        # Act  
        with self.assertRaises(ValueError) as context:
            mortgage.rate = 'INVALID_RATE'

        # Assert
        expected = "Rate provided is invalid."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_modify_frequency_to_valid(self):
        """
        Test the mutator for frequency: Modify the frequency to a valid 
        value and verify the result.
        """
        # Arrange
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)

        # Act
        mortgage.frequency = 'BI_WEEKLY'

        # Assert
        self.assertEqual(mortgage.frequency, PaymentFrequency['BI_WEEKLY'])

    def test_modify_frequency_to_invalid(self):
        """
        Test the mutator for frequency: Modify the frequency to an 
        invalid value and verify that ValueError is raised.
        """
        # Arrange
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)

        # Act  
        with self.assertRaises(ValueError) as context:
            mortgage.frequency = 'INVALID_FREQUENCY'

        # Assert
        expected = "Frequency provided is invalid."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_modify_amortization_to_valid(self):
        """
        Test the mutator for amortization: Modify the amortization 
        period to a valid value and verify the result.
        """
        # Arrange
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)

        # Act
        mortgage.amortization = 25

        # Assert
        self.assertEqual(mortgage.amortization, 25)

    def test_modify_amortization_to_invalid(self):
        """
        Test the mutator for amortization: Modify the amortization 
        period to an invalid value and verify that ValueError is raised.
        """
        # Arrange
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 20)

        # Act  
        with self.assertRaises(ValueError) as context:
            mortgage.amortization = 40

        # Assert
        expected = "Amortization provided is invalid."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_calculate_payment(self):
        """
        Test cases for the calculate_payment method.
        """
        # Arrange
        mortgage = Mortgage(682912.43, 'FIXED_1', 'MONTHLY', 10)

        # Act
        result = mortgage.calculate_payment()

        # Assert
        self.assertAlmostEqual(result, 7578.30, places=2)

    def test_mortgage_str_monthly(self):
        """Test for monthly payment frequency"""
        mortgage = Mortgage(682912.43, "FIXED_5", "MONTHLY", 30)
        expected_str = (
            "Mortgage Amount: $682,912.43\n"
            "Rate: 5.19%\n"  
            "Amortization: 30\n"
            "Frequency: Monthly -- Calculated Payment: $3,745.73"  
        )
        self.assertEqual(str(mortgage), expected_str)
    
    def test_mortgage_str_biweekly(self):
        """Test for biweekly payment frequency"""
        mortgage = Mortgage(682912.43, "FIXED_5", "BI_WEEKLY", 30)
        expected_str = (
            "Mortgage Amount: $682,912.43\n"
            "Rate: 5.19%\n"
            "Amortization: 30\n"
            "Frequency: Bi_Weekly -- Calculated Payment: $1,727.96"  
        )
        self.assertEqual(str(mortgage), expected_str)

    def test_mortgage_str_weekly(self):
        """Test for weekly payment frequency"""
        mortgage = Mortgage(682912.43, "FIXED_5", "WEEKLY", 30)
        expected_str = (
            "Mortgage Amount: $682,912.43\n"
            "Rate: 5.19%\n"
            "Amortization: 30\n"
            "Frequency: Weekly -- Calculated Payment: $863.80" 
        )
        self.assertEqual(str(mortgage), expected_str)

    def test_repr(self):
        # Arrange
        loan_amount = 250000.0
        rate = "FIXED_5"
        amortization = 25
        frequency = "MONTHLY"
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        result = repr(mortgage)

        # Assert
        expected_repr = (
    "Mortgage(loan_amount=250000.00, rate=0.0519, "
    "amortization=25, frequency='12')"
)
        self.assertEqual(result, expected_repr)

if __name__ == "__main__":
    unittest.main()
