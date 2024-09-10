from .schemas import UserCreateSchema
from . import utils


def create_access_token(user: UserCreateSchema):
    payload: dict = {
        "sub": user.email,
    }

    return utils.encode_jwt(payload=payload)

