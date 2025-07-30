__author__ = "Lichao Huang"
__version__ = "1.0.0"

from mortgage.payment_frequency import PaymentFrequency

class Mortgage:
    _years = [5, 10, 15, 20, 25, 30]
    def __init__(self, Loan_Amount: float, Annual_Interest_Rate: float, Amortization: int, Frequency: PaymentFrequency):
        if isinstance(Loan_Amount,(int,float)):
            if Loan_Amount <= 0:
                raise ValueError("Loan Amount must be a value greater than zero.")
            self._Loan_Amount = Loan_Amount
        else:
            raise TypeError("Loan amount must be a value of a numeric type.")
        
        
        if isinstance(Annual_Interest_Rate,(int, float)):
            if Annual_Interest_Rate > 1:
                raise ValueError("Annual interest rate must be a value greater than zero and less than or equal to 1.")
            if Annual_Interest_Rate <= 0:
                raise ValueError("Annual interest rate must be a value greater than zero and less than or equal to 1.")
            self._Annual_Interest_Rate = Annual_Interest_Rate
        else:
            raise TypeError("Annual interest rate must be a value of a numeric type.")
        
        if Amortization in Mortgage._years:
            self._Amortization = Amortization
        else:
            raise ValueError("Amortization must be a value in [5, 10, 15, 20, 25, 30].")
        
        if isinstance(Frequency, PaymentFrequency):
            self._Frequency = Frequency
        else:
            raise ValueError("Frequency must be a value of PaymentFrequency type.")
        