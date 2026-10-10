from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.app.api.deps import get_db
from src.app.modules.auth.schemas import RegisterSchema
from src.app.modules.auth.service import register_user

router = APIRouter()


@router.post("/register")
def register(body: RegisterSchema, db: Session = Depends(get_db)):
    body = body.model_dump()
    new_user = register_user(body, db)
    return {"success": True, "message": "Registered Successfully..", "data": new_user}
