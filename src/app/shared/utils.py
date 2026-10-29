from sqlalchemy.orm import Session
from fastapi import Request, status, Depends
import jwt
from jwt.exceptions import InvalidTokenError
from src.app.core.exceptions import AppException
from src.app.core.config import settings
from src.app.modules.user.models import UserModel
from src.app.api.deps import get_db


# check for token validation and return user
def is_user_authenticated(request: Request, db: Session = Depends(get_db)):
    token = request.headers.get("authorization")

    if not token:
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED, message="Unauthorized Access"
        )

    try:
        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)

    except InvalidTokenError as exc:
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED, message="Invalid Token"
        ) from exc

    user_id = data["id"]

    user = db.query(UserModel).filter(UserModel.id == user_id).first()

    if not user:
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED, message="Invalid Token"
        )

    return user
