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

    @property
    def Loan_Amount(self):
        return self._Loan_Amount
    
    @property
    def annual_interest_rate(self):
        return self._Annual_Interest_Rate

    @property
    def amortization(self):
        return self._Amortization
    
    @property
    def frequency(self):
        return self._Frequency
    

    @Loan_Amount.setter
    def Loan_Amount(self, value):
        if isinstance(value, (int, float)):
            if value <= 0:
                raise ValueError("Loan Amount must be a value greater than zero.")
            self._Loan_Amount = value
        else:
            raise TypeError("Loan amount must be a value of a numeric type.")
        
    @annual_interest_rate.setter
    def annual_interest_rate(self, value):
        if isinstance(value, (int, float)):
            if 0 < value <= 1:
                self._Annual_Interest_Rate = value
            else:
                raise ValueError("Annual interest rate must be greater than 0 and less than or equal to 1.")
        else:
            raise TypeError("Annual interest rate must be numeric.")
        
    @amortization.setter
    def amortization(self, value):
        if value not in Mortgage._years:
            raise ValueError("Amortization must be a value in [5, 10, 15, 20, 25, 30].")
        self._Amortization = value
    
    @frequency.setter
    def frequency(self, value):
        if isinstance(value, PaymentFrequency):
            self._Frequency = value
        else:
            raise ValueError("Frequency must be a value of PaymentFrequency type.")
