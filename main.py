"""This module demonstrates your understanding of object-oriented
programming.

Below each of the comments, code the statement or statements to satisfy
the requirement specified in the comment.
"""

__author__ = "Lichao Huang"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

from mortgage.mortgage import Mortgage
from mortgage.payment_frequency import PaymentFrequency
# 1. Create an instance of the Mortgage class. Initialize the object
#    using values of your choosing. NOTE: This object will be used for 
#    the following 4 questions.
mortgage = Mortgage(10000, 0.05, 5, PaymentFrequency.MONTHLY)

# 2. Print the official string representation of the object.
print(repr(mortgage))

# 3. Print the payment amount for the mortgage. Format the payment 
#    amount as currency.
print(f"${mortgage.get_payment()}")

# 4. Update the state of the object such that all attributes values are 
#    different than what they were initialized to.
mortgage._Loan_Amount = 2000000
mortgage._Annual_Interest_Rate = 0.03
mortgage._Amortization = 10
mortgage._Frequency = PaymentFrequency.WEEKLY

# 5. Choose any attribute of the object and print it's current state.
print(f"${mortgage.get_payment()}")

# 6. Attempt to create another instance of the Mortgage class. The 
#    statement must use one value that will cause the initialization
#    to fail. Prevent the script from abnormally ending and print the
#    error message to the console.
try:
    bad_mortgage = Mortgage(-5000, 0.04, 10, PaymentFrequency.MONTHLY)
except Exception as error:
    print(error)