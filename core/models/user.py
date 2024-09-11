from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contacting import Contacting

class User(Base):
    __tablename__ = "users"

    firstname: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[bytes] = mapped_column(nullable=False)

    contactings: Mapped[list["Contacting"]] = relationship(back_populates="user")