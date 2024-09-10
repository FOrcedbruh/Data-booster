import jwt
from core.settings import settings
import datetime
import bcrypt
from fastapi import Form
from .schemas import UserCreateSchema

def encode_jwt(
        payload: dict,
        algorithm: str = "HS256",
        secret: str = settings.token.secret
    ) -> str:
    payload["exp"] = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=30)
    return jwt.encode(key=secret, algorithm=algorithm, payload=payload)

def decode_jwt(
        token: str,
        algorithm: str = "HS256",
        secret: str = settings.token.secret,
    ) -> dict:
    return jwt.decode(jwt=token, key=secret, algorithms=[algorithm])


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(salt=bcrypt.gensalt(), password=password.encode())

def validation_password(hashed_password: bytes, password: str) -> bool:
    return bcrypt.checkpw(hashed_password=hashed_password, password=password.encode())


def RegForm(email: str = Form(), password: str = Form()) -> UserCreateSchema:
    return UserCreateSchema(
        email=email,
        password=password
    )
