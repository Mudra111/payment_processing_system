from fastapi import FastAPI
from src.app.api.v1.router import api_router as api_router_v1
from src.app.infrastructure.database.session import engine
from src.app.infrastructure.database.base import Base
from fastapi.exceptions import RequestValidationError
from app.core.exception_handler import (
    validation_exception_handler,
    app_exception_handler,
    internal_exception_handler,
)
from src.app.core.exceptions import AppException

Base.metadata.create_all(engine)

app = FastAPI()

app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.add_exception_handler(AppException, app_exception_handler)

app.add_exception_handler(Exception, internal_exception_handler)

# add auth route
app.include_router(api_router_v1, prefix="/api/v1")
