from src.app.modules.auth.schemas import RegisterSchema
from sqlalchemy.orm import Session


def register_user(body: RegisterSchema, db: Session):
    new_user = body
    return new_user
