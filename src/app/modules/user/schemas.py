from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
