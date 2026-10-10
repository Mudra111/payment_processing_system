from pydantic import BaseModel


class RegisterSchema(BaseModel):
    name: str
    username: str
    email: str
    password: str
