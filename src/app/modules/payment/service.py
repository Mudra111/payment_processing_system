from src.app.modules.payment.schemas import CreatePaymentSchema
from sqlalchemy.orm import Session
from src.app.modules.user.schemas import UserSchema
from src.app.core.exceptions import AppException
from fastapi import status
from src.app.modules.user.models import UserModel
from src.app.modules.wallet.models import WalletModel
from src.app.modules.payment.models import PaymentModel


def create_payment(body: CreatePaymentSchema, db: Session, user: UserSchema):
    # body = body.model_dump()

    # Check if Sender_id is same as user id we get from jwt token
    if body.sender_id != user.id:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Unauthorized to send payment with this sender_id",
        )

    sender_user = user

    # Check if sender user's wallet exist or not
    sender_wallet = (
        db.query(WalletModel).filter(WalletModel.user_id == sender_user.id).first()
    )

    if not sender_wallet:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Sender user wallet not found",
        )

    # Check if receiver exist or not
    receiver_user = db.query(UserModel).filter(UserModel.id == body.receiver_id).first()

    if not receiver_user:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND, message="Receiver not found"
        )

    # Check if receiver user's wallet exist or not
    receiver_wallet = (
        db.query(WalletModel).filter(WalletModel.user_id == receiver_user.id).first()
    )

    if not receiver_wallet:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Receiver user wallet not found",
        )

    # Check if sender user has enough budget for this payment or not
    if sender_wallet.balance < body.amount:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Insufficient balance for this transaction",
        )

    # Create payment with status PENDING
    new_payment = PaymentModel(
        sender_id=body.sender_id,
        receiver_id=body.receiver_id,
        amount=body.amount,
        idempotency_key=body.idempotency_key,
        currency=body.currency,
        description=body.description,
        payment_reference=body.payment_reference,
    )

    db.add(new_payment)

    db.commit()
    db.refresh(new_payment)

    return new_payment
