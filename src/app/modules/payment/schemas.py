from pydantic import BaseModel
from decimal import Decimal


class CreatePaymentSchema(BaseModel):
    sender_id: int
    receiver_id: int
    amount: Decimal
    currency: str
    idempotency_key: str
    description: str
    payment_reference: str
