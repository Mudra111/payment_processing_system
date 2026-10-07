from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.app.core.config import settings

engine = create_engine(url=settings.DB_CONNECTION)

LocalSession = sessionmaker(bind=engine)
