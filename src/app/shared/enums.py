from enum import Enum


class CurrencyEnum(str, Enum):
    INR = "INR"
    USD = "USD"
    GBP = "GBP"


class PaymentStatusEnum(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
