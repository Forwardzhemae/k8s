from fastapi import APIRouter, HTTPException, status, Response
from sqlalchemy import select
from app.services.gamers_service import get_gamers_with_cache
from app.core.config import config, security
from app.db.session import SessionDep, engine
from app.models.base import Base
from app.models.gamers import Gamer, UserLoginSchema
from app.schemas.gamers import GamerCreate, GamerOut
from app.core.redis import get_redis

router = APIRouter(prefix="/gamers", tags=["gamers"])

@router.post("/setup", status_code=status.HTTP_200_OK)
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return {"ok": True}

@router.post("/", response_model=GamerOut, status_code=status.HTTP_201_CREATED)
async def add_gamer(data: GamerCreate, session: SessionDep):
    gamer = Gamer(
        name=data.name,
        sec_name=data.sec_name,
        email=str(data.email) if data.email else None,
        game_name=data.game_name,
    )
    redis = get_redis()
    session.add(gamer)
    await session.commit()
    await session.refresh(gamer)
    await redis.delete("gamers:all")
    return gamer

@router.get("/", response_model=list[GamerOut])
async def get_gamers(session: SessionDep):
    result = await session.execute(select(Gamer))
    return await get_gamers_with_cache(session)

# JWT # TOKEN IN CONFIG.PY
@router.post("/login")
def login(credentials: UserLoginSchema, response: Response):
    if credentials.username == "Nurly" and credentials.password == "1234":
        token = security.create_access_token(uid="123456")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return{"access token": token}
    raise HTTPException(status_code=401, detail="incorrect password or login")

@router.get("/protected")
def protected():
    return {"success": True}