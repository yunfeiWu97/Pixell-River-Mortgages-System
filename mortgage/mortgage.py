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
        loan_amount (float): The amount of the mortgage loan.
        rate (str): The annual interest rate as a string (e.g., "FIXED_5").
        frequency (str): The payment frequency as a string (e.g., "MONTHLY").
        amortization (int): The number of years for the mortgage loan repayment.

        Raises:
        ValueError: Raise when any of the provided values are invalid.
        """

        # Validate Loan Amount
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = loan_amount

        # Validate Rate
        try:
            self.__rate = MortgageRate[rate]
        except KeyError:
            raise ValueError("Rate provided is invalid.")

        # Validate Frequency
        try:
            self.__frequency = PaymentFrequency[frequency]
        except KeyError:
            raise ValueError("Frequency provided is invalid.")

        # Validate Amortization
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = amortization
    




    # Accessor and Mutator for Loan Amount
    @property
    def loan_amount(self):
        """Returns the loan amount."""
        return self.__loan_amount

    @loan_amount.setter
    def loan_amount(self, value: float):
        """
        Sets the loan amount with validation.

        Args:
            value (float): The new loan amount.
        
        Raises:
            ValueError: If the new loan amount is <= 0.
        """
        if value <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = value











    @property
    def rate(self):
        """
        Get the mortgage rate.
        """
        return self.__rate

    @rate.setter
    def rate(self, value: str):
        """
        Set the mortgage rate, converting it to a MortgageRate enum.

        Arg:
            value (str): The new rate value.

        Raises:
            ValueError: If the provided rate is invalid.
        """
        try:
            self.__rate = MortgageRate[value]  # Ensure value is stored as MortgageRate enum
        except KeyError:
            raise ValueError("Rate provided is invalid.")
        








    @property
    def frequency(self):
        """
        Get the payment frequency.
        """
        return self.__frequency

    @frequency.setter
    def frequency(self, value: str):
        """
        Set the payment frequency, converting it to a PaymentFrequency enum.

        Arg:
            value (str): The new frequency value.

        Raises:
            ValueError: If the provided frequency is invalid.
        """
        try:
            self.__frequency = PaymentFrequency[value]  # Convert string to PaymentFrequency enum
        except KeyError:
            raise ValueError("Frequency provided is invalid.")
        







    # Accessor and Mutator for Amortization
    @property
    def amortization(self):
        """
        Get the amortization period in years.
        """        
        return self.__amortization

    @amortization.setter
    def amortization(self, value: int):
        """
        Sets the amortization period with validation.

        Args:
            value (int): The new amortization period.
        
        Raises:
            ValueError: If the new amortization period is invalid.
        """
        if value not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = value









    def calculate_payment(self) -> float:
        """
        Calculates the mortgage payment based on the loan amount, 
        interest rate, frequency, and amortization period.
        """
        P = self.__loan_amount
        rate = self.__rate.value
        n = self.__amortization * self.__frequency.value
        i = rate / self.__frequency.value
        
        payment = P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        return round(payment, 2)