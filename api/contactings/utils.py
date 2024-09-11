from fastapi import Body
from .schemas import ConCreateSchema

def ConForm(text: str = Body(), user_id: int = Body()) -> ConCreateSchema:
    return ConCreateSchema(
        text=text,
        user_id=user_id
    )
