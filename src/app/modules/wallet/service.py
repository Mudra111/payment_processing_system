from src.app.modules.wallet.models import WalletModel
from sqlalchemy.orm import Session


def initialize_wallet(user_id: int, db: Session):
    new_wallet = WalletModel(user_id=user_id)
    db.add(new_wallet)
    db.flush()
    # print(new_wallet.user_id, new_wallet.id, new_wallet.balance)
    return new_wallet
