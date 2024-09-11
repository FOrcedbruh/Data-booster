from .schemas import UserCreateSchema
from . import utils

def create_access_token(user: UserCreateSchema) -> str:
    payload: dict = {
        "sub": user.email,
    }

    return utils.encode_token(payload=payload)

