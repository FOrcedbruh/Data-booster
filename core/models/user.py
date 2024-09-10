from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[bytes] = mapped_column(nullable=False)