from src.app.modules.auth.schemas import RegisterSchema, LoginSchema
from sqlalchemy.orm import Session
from src.app.modules.user.models import UserModel
from fastapi import HTTPException, status
from src.app.core.security import hash_password, verify_password
from src.app.core.config import settings
from src.app.core.exceptions import AppException

# jwt token
from datetime import datetime, timedelta
import jwt


def register_user(body: RegisterSchema, db: Session):
    try:
        is_email = db.query(UserModel).filter(UserModel.email == body["email"]).first()

        if is_email:
            raise AppException(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Email Already Exist...",
            )

        is_username = (
            db.query(UserModel).filter(UserModel.username == body["username"]).first()
        )

        if is_username:
            raise AppException(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Username Already Exist...",
            )

        hashed_password = hash_password(body["password"])

        new_user = UserModel(
            name=body["name"],
            email=body["email"],
            username=body["username"],
            hash_password=hashed_password,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

    except Exception:
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Something went wrong",
        )

    return new_user


def login_user(body: LoginSchema, db: Session):
    try:
        is_user = db.query(UserModel).filter(UserModel.email == body["email"]).first()

        if not is_user:
            raise AppException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="You Entered wrong Email",
            )

        is_verified = verify_password(body["password"], is_user.hash_password)

        if not is_verified:
            raise AppException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="You Entered wrong password",
            )

        exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)

        token = jwt.encode(
            {"id": is_user.id, "exp": exp_time.timestamp()},
            settings.SECRET_KEY,
            settings.ALGORITHM,
        )

    except Exception:
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Something went wrong",
        )

    return token
