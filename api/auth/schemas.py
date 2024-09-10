from pydantic import BaseModel, EmailStr




class UserSchema(BaseModel):
    id: int
    email: EmailStr
    password: bytes

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str