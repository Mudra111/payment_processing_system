from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.app.api.deps import get_db
from src.app.modules.wallet.service import get_balance
from src.app.shared.utils import is_user_authenticated
from src.app.modules.user.models import UserModel

router = APIRouter()


@router.get("/balance")
def getBalance(
    db: Session = Depends(get_db), user: UserModel = Depends(is_user_authenticated)
):
    wallet = get_balance(db, user)
    return {"success": True, "message": "Wallet Fetched Successfully..", "data": wallet}
