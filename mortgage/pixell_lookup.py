"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: Yunfei Wu
Date: 2024-11-08
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum

class MortgageRate(Enum):
    """
    Enumeration for different mortgage rates.
    FIXED_5: 5-year fixed rate at 5.19%
    FIXED_3: 3-year fixed rate at 5.89%
    FIXED_1: 1-year fixed rate at 5.99%
    VARIABLE_5: 5-year variable rate at 6.49%
    VARIABLE_3: 3-year variable rate at 6.69%
    VARIABLE_1: 1-year variable rate at 6.79%
    """
    FIXED_5 = 0.0519
    FIXED_3 = 0.0589
    FIXED_1 = 0.0599
    VARIABLE_5 = 0.0649
    VARIABLE_3 = 0.0669
    VARIABLE_1 = 0.0679

class PaymentFrequency(Enum):
    """
    Enumeration for different payment frequency options.
    MONTHLY: 12 payments per year (monthly)
    BI_WEEKLY: 26 payments per year (bi-weekly)
    WEEKLY: 52 payments per year (weekly)
    """
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52
    
VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}

