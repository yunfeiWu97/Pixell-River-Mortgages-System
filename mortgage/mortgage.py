"""
Description: A class meant to manage Mortgage options.
Author: Yunfei Wu
Date: 2024-11-08
Usage: Create an instance of the Mortgage class to manage mortgage 
records and calculate payments.
"""

from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    """
    A class to represent a mortgage loan.
    """

    def __init__(self, loan_amount: float, rate: str, frequency: str, amortization: int):
        """
        Initialize a new mortgage with the provided parameters.

        Args:
        Loan_amount (float): The amount of the mortgage loan.
        Rate (str): The annual interest rate as a string (e.g., "FIXED_5").
        Frequency (str): The payment frequency as a string (e.g., "MONTHLY").
        Amortization (int): The number of years for the mortgage loan repayment.

        Raises:
        ValueError: Raise when any of the provided values are invalid.
        """

        # Loan Amount Validation
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = loan_amount

        # Rate Validation
        try:
            self.__rate = MortgageRate[rate]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")

        # Frequency Validation
        try:
            self.__frequency = PaymentFrequency[frequency]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")

        # Amortization Validation
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = amortization
   
    @property
    def loan_amount(self):
        """Accessor for the loan amount."""
        return self.__loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        """Mutator for the loan amount with validation."""
        if value <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = value