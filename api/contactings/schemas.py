from pydantic import BaseModel, Field

class ConCreateSchema(BaseModel):
    user_id: int
    text: str = Field(max_length=200)
