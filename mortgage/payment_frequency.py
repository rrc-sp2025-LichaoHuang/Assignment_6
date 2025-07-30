__author__ = "Lichao Huang"
__version__ = "1.0.0"

from enum import Enum

class PaymentFrequency(Enum):
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52