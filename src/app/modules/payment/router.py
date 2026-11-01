from fastapi import APIRouter, Depends
from src.app.api.deps import get_db
from sqlalchemy.orm import Session
from src.app.modules.user.schemas import UserSchema
from src.app.shared.utils import is_user_authenticated
from src.app.modules.payment.schemas import CreatePaymentSchema
from src.app.modules.payment.service import create_payment

router = APIRouter()


@router.post("/create")
def create(
    body: CreatePaymentSchema,
    db: Session = Depends(get_db),
    user: UserSchema = Depends(is_user_authenticated),
):
    return create_payment(body, db, user)
