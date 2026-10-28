from src.app.modules.wallet.models import WalletModel
from sqlalchemy.orm import Session
from src.app.modules.user.models import UserModel
from src.app.core.exceptions import AppException
from fastapi import status


def initialize_wallet(user_id: int, db: Session):
    new_wallet = WalletModel(user_id=user_id)
    db.add(new_wallet)
    db.flush()
    # print(new_wallet.user_id, new_wallet.id, new_wallet.balance)
    return new_wallet


def get_balance(db: Session, user: UserModel):
    wallet = db.query(WalletModel).filter(WalletModel.user_id == user.id).first()

    if not wallet:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND, message="Wallet not found"
        )

    return wallet
