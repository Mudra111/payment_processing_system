from fastapi import APIRouter
from src.app.modules.auth.router import router as auth_router
from src.app.modules.user.router import router as user_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])

api_router.include_router(user_router, prefix="/user", tags=["User"])
