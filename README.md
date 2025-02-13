# Mortgage Management System

## Description

This project is designed to manage and validate mortgage data, ensuring correct calculations and adherence to defined rules. It includes a **Mortgage** class for handling mortgage records and calculating payments, along with a suite of unit tests to verify functionality.

## Features

- **Mortgage Class**: Handles mortgage records, including loan amount, interest rate, payment frequency, and amortization period.
- **Validation**: Ensures valid inputs for loan amount, rate type, payment frequency, and amortization period.
- **Payment Calculation**: Computes monthly, bi-weekly, or weekly mortgage payments.
- **Unit Testing**: Provides test cases for validation, accessor/mutator methods, and calculation accuracy.
- **Error Handling**: Catches and reports invalid mortgage entries from an input file.

## Files

- `mortgage.py` - Defines the **Mortgage** class and its functionality.
- `mortgage_tests.py` - Unit tests for verifying mortgage validation and calculations.
- `pixell_river_mortgages.txt` - Sample mortgage data used for testing.
- `client_program.py` - Reads mortgage data from a file and processes payments.

## Usage

1. **Run Unit Tests**:
   
   ```sh
   python -m unittest mortgage_tests.py
   ```

2. **Process Mortgage Data**:
   
   ```sh
   python client_program.py
   ```

## Author

**Yunfei Wu**  

Date: 2024-11-08
