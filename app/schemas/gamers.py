from pydantic import BaseModel, EmailStr, Field

class GamerCreate(BaseModel):
    name: str
    sec_name: str | None = None
    email: EmailStr | None = None
    game_name: str | None = None

class GamerOut(GamerCreate):
    id: int
