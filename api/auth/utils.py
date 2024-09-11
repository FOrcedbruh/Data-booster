import jwt
from core.settings import settings
import datetime
import bcrypt
from fastapi import Body
from .schemas import UserCreateSchema, UserLoginSchema



def encode_token(
        payload: dict,
        algorithm: str = "HS256",
        secret: str = settings.token.secret,
    ) -> str:
    payload["exp"] = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=30)
    payload["iat"] = datetime.datetime.now(datetime.UTC)
    return jwt.encode(key=str(secret), payload=payload, algorithm=algorithm)




def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(salt=bcrypt.gensalt(), password=password.encode())

def validation_password(hashed_password: bytes, password: str) -> bool:
    return bcrypt.checkpw(hashed_password=hashed_password, password=password.encode())


def RegForm(email: str = Body(), password: str = Body(), firstname: str = Body(), surname: str = Body()) -> UserCreateSchema:
    return UserCreateSchema(
        email=email,
        password=password
    )

def LogForm(email: str = Body(), password: str = Body()) -> UserLoginSchema:
    return UserLoginSchema(
        email=email,
        password=password
    )