"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: Yunfei Wu
Date: 2024-11-08
"""

### REQUIREMENT
### ADD IMPORT STATEMENT FOR THE MORTGAGE CLASS
from mortgage.mortgage import Mortgage

try:
    ### REQUIREMENT
    ### ENCLOSE THE FOLLOWING 'WITH OPEN' BLOCK IN A 'TRY-EXCEPT' BLOCK WHICH 
    ### WILL CATCH A 'FILENOTFOUNDERROR' EXCEPTION
    with open ("data\\pixell_river_mortgages.txt","r") as input:
        print("**************************************************")
        
        for data in input:
            items = data.split(",")
            
            try:
                amount = float(items[0])    # Convert amount to float
                rate = items[1]     # Convert rate to float
                amortization = int(items[2])    # Convert amortization to int
                frequency = items[3]    # Remove any trailing spaces

                ### REQUIREMENT:
                ### INSTANTIATE A MORTGAGE OBJECT USING THE VALUES
                ### FOR AMOUNT, RATE, FREQUENCY AND AMORTIZATION ABOVE.
                mortgage = Mortgage(amount, rate, frequency, amortization)
                
                ### REQUIREMENT:
                ### PRINT THE MORTGAGE OBJECT
                print(mortgage)

            except ValueError as e:
                # This except block will catch Explicit exceptions: 
                # Those raised by the programmer in the Mortgage class.
                print(f"Data: {data.strip()} caused Exception: {e}")
            
            except Exception as e:
                # This except block will catch Implicit exceptions:  
                # Those raised through normal execution.
                print(f"Data: {data.strip()} caused Exception: {e}")
            finally:
                print("**************************************************")

except FileNotFoundError as e:
    print(f"Error: {e}")
