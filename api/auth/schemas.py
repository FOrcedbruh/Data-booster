from pydantic import BaseModel, EmailStr




class UserSchema(BaseModel):
    id: int
    email: EmailStr
    password: bytes
    firstname: str
    surname: str

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str
    firstname: str
    surname: str

class UserLoginSchema(BaseModel):
    email: str
    password: str