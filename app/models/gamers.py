from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base
from pydantic import BaseModel

class Gamer(Base):
    __tablename__ = "gamers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    sec_name: Mapped[str | None]
    email: Mapped[str | None]
    game_name: Mapped[str | None]

class UserLoginSchema(BaseModel):
    username: str
    password: str