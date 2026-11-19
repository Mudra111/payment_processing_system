from pydantic import BaseModel, EmailStr


class RegisterSchema(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str
    currency: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str
