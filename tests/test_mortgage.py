import unittest
from unittest import TestCase, main
from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import MagicMock
from mortgage.mortgage import Mortgage
from mortgage.payment_frequency import PaymentFrequency

__author__ = "Lichao Huang"
__version__ = "1.0.0"



class TestMortgage(unittest.TestCase):

    def test_invalid_loan_amount_type(self):
        # Arrange 
        expected = "Loan amount must be a value of a numeric type."
        # Act
        with self.assertRaises(TypeError) as context:
            Mortgage(Loan_Amount="aaa", Annual_Interest_Rate=0.5, Amortization=25, Frequency=PaymentFrequency.MONTHLY)
        self.assertEqual(expected,str(context.exception))

    def test_negative_loan_amount_value(self):
        # Arrange 
        expected = "Loan Amount must be a value greater than zero."
        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(Loan_Amount=-1, Annual_Interest_Rate=0.5, Amortization=25, Frequency=PaymentFrequency.MONTHLY)
        self.assertEqual(expected,str(context.exception))

    def test_zero_loan_amount_value(self):
        # Arrange 
        expected = "Loan Amount must be a value greater than zero."
        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(0, Annual_Interest_Rate=0.5, Amortization=25, Frequency=PaymentFrequency.MONTHLY)
        self.assertEqual(expected,str(context.exception))

    def test_invalid_interest_type(self):
        # Arrange 
        expected = "Annual interest rate must be a value of a numeric type."
        # Act
        with self.assertRaises(TypeError) as context:
            Mortgage(Loan_Amount=1, Annual_Interest_Rate="five", Amortization=25, Frequency=PaymentFrequency.MONTHLY)
        self.assertEqual(expected,str(context.exception))

    def test_negative_interest_value(self):
        # Arrange 
        expected = "Annual interest rate must be a value greater than zero and less than or equal to 1."
        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(Loan_Amount=1, Annual_Interest_Rate= -1, Amortization=25, Frequency=PaymentFrequency.MONTHLY)
        self.assertEqual(expected,str(context.exception))

    def test_zero_interest_value(self):
        # Arrange 
        expected = "Annual interest rate must be a value greater than zero and less than or equal to 1."
        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(Loan_Amount=1, Annual_Interest_Rate= 0, Amortization=25, Frequency=PaymentFrequency.MONTHLY)
        self.assertEqual(expected,str(context.exception))

    def test_greater_then_one_interest_value(self):
        # Arrange 
        expected = "Annual interest rate must be a value greater than zero and less than or equal to 1."
        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(Loan_Amount=1, Annual_Interest_Rate= 1.1, Amortization=25, Frequency=PaymentFrequency.MONTHLY)
        self.assertEqual(expected,str(context.exception))

    def test_invalid_amortization_value(self):
        # Arrange 
        expected = "Amortization must be a value in [5, 10, 15, 20, 25, 30]."
        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(Loan_Amount=1, Annual_Interest_Rate=0.5, Amortization=7, Frequency=PaymentFrequency.MONTHLY)
        self.assertEqual(expected,str(context.exception))

    def test_invalid_frequency_type(self):
        # Arrange 
        expected = "Frequency must be a value of PaymentFrequency type."
        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(Loan_Amount=1, Annual_Interest_Rate=0.5, Amortization=25, Frequency="Monthly")
        self.assertEqual(expected,str(context.exception))

    def test_init_initializes_attributes(self):
        loan_amount = 300000
        annual_interest_rate = 0.045
        amortization = 20
        frequency = PaymentFrequency.MONTHLY

        mortgage = Mortgage(loan_amount, annual_interest_rate, amortization, frequency)

        self.assertEqual(mortgage._Loan_Amount, loan_amount)
        self.assertEqual(mortgage._Annual_Interest_Rate, annual_interest_rate)
        self.assertEqual(mortgage._Amortization, amortization)
        self.assertEqual(mortgage._Frequency, frequency)

    ####################  Mutators for Loan Amount  ####################

    def test_mutators_for_Loan_Amount_Valid(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = 200
        #act
        mortgage.Loan_Amount = 200
        #assert
        self.assertEqual(expected, mortgage.Loan_Amount)

    def test_mutators_for_Loan_Amount_TypError(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = "Loan amount must be a value of a numeric type."
        #act
        with self.assertRaises(TypeError) as context:
            mortgage.Loan_Amount = "aa"

        #assert
        self.assertEqual(expected, str(context.exception))

    def test_mutators_for_Loan_Amount_0(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = "Loan Amount must be a value greater than zero."
        #act
        with self.assertRaises(ValueError) as context:
            mortgage.Loan_Amount = 0

        #assert
        self.assertEqual(expected, str(context.exception))

    def test_mutators_for_Loan_Amount_negative(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = "Loan Amount must be a value greater than zero."
        #act
        with self.assertRaises(ValueError) as context:
            mortgage.Loan_Amount = -1

        #assert
        self.assertEqual(expected, str(context.exception))

    ####################  Mutators for Annual Interest Rate  ####################

    def test_mutators_Annual_Interest_Rate_Valid(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = 0.66
        #act
        mortgage._Annual_Interest_Rate = 0.66
        #assert
        self.assertEqual(expected, mortgage._Annual_Interest_Rate)

    def test_mutators_for_Annual_Interest_Rate_TypError(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = "Loan amount must be a value of a numeric type."
        #act
        with self.assertRaises(TypeError) as context:
            mortgage.annual_interest_rate = "aa"

        #assert
        self.assertEqual(expected, str(context.exception))

    def test_mutators_for_Annual_Interest_Rate_0(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = "Annual interest rate must be greater than 0 and less than or equal to 1."
        #act
        with self.assertRaises(ValueError) as context:
            mortgage.annual_interest_rate = 0

        #assert
        self.assertEqual(expected, str(context.exception))

    def test_mutators_for_Annual_Interest_Rate_negative(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = "Annual interest rate must be greater than 0 and less than or equal to 1."
        #act
        with self.assertRaises(ValueError) as context:
            mortgage.annual_interest_rate = -1

        #assert
        self.assertEqual(expected, str(context.exception))

    def test_mutators_for_Annual_Interest_Rate_grater_then_1(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = "Annual interest rate must be greater than 0 and less than or equal to 1."
        #act
        with self.assertRaises(ValueError) as context:
            mortgage.annual_interest_rate = 1.1

        #assert
        self.assertEqual(expected, str(context.exception))

    ####################  Mutators for Amortization  ####################

    def test_mutators_Amortization_valid(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = 30
        #act
        mortgage.amortization = 30
        #assert
        self.assertEqual(expected, mortgage.amortization)

    def test_mutators_Amortization_invalid_aa(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = "Amortization must be a value in [5, 10, 15, 20, 25, 30]."
        #act
        with self.assertRaises(ValueError) as context:
            mortgage.amortization = "aa"

        #assert
        self.assertEqual(expected, str(context.exception))

    def test_mutators_Amortization_invalid_11(self):
        #arrange
        mortgage = Mortgage(100, 0.5, 5, Frequency=PaymentFrequency.MONTHLY)
        expected = "Amortization must be a value in [5, 10, 15, 20, 25, 30]."
        #act
        with self.assertRaises(ValueError) as context:
            mortgage.amortization = 11

        #assert
        self.assertEqual(expected, str(context.exception))

    ####################  Mutators for Frequency  ####################

    def test_frequency_setter_valid(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        mortgage.frequency = PaymentFrequency.BI_WEEKLY
        self.assertEqual(mortgage.frequency, PaymentFrequency.BI_WEEKLY)

    def test_frequency_setter_invalid_type(self):
        mortgage = Mortgage(100000, 0.05, 25, PaymentFrequency.MONTHLY)
        expected = "Frequency must be a value of PaymentFrequency type."
        with self.assertRaises(ValueError) as context:
            mortgage.frequency = "WEEKLY" 
        self.assertEqual(str(context.exception),expected)


if __name__ == '__main__':
    unittest.main()