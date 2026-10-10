from src.app.infrastructure.database.base import Base
from sqlalchemy import Column, String, Integer


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hash_password = Column(String, nullable=False)
