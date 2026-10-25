from src.app.modules.auth.schemas import RegisterSchema, LoginSchema
from sqlalchemy.orm import Session
from src.app.modules.user.models import UserModel
from fastapi import status
from src.app.core.security import hash_password, verify_password
from src.app.core.config import settings
from src.app.core.exceptions import AppException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from src.app.modules.wallet.service import initialize_wallet

# jwt token
from datetime import datetime, timedelta
import jwt


def register_user(body: RegisterSchema, db: Session):
    existing_email = db.query(UserModel).filter(UserModel.email == body.email).first()

    if existing_email:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Email Already Exist",
        )

    existing_username = (
        db.query(UserModel).filter(UserModel.username == body.username).first()
    )

    if existing_username:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Username Already Exist",
        )

    hashed_password = hash_password(body.password)

    new_user = UserModel(
        name=body.name,
        email=body.email,
        username=body.username,
        hash_password=hashed_password,
    )

    try:
        db.add(new_user)
        db.flush()

        # Call create wallet method here
        initialize_wallet(user_id=new_user.id, db=db)

        db.commit()
        db.refresh(new_user)

    except IntegrityError as exc:
        db.rollback()

        raise AppException(
            status_code=status.HTTP_409_CONFLICT,
            message="A user with these details already exists",
        ) from exc

    except SQLAlchemyError:
        db.rollback()
        raise

    return new_user


def login_user(body: LoginSchema, db: Session):
    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()

    if not is_user or not verify_password(body.password, is_user.hash_password):
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Invalid Email or Password",
        )

    exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)

    token = jwt.encode(
        {"id": is_user.id, "exp": exp_time.timestamp()},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    return token
