from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routes import api_router
from app.models.base import Base
from app.db.session import engine
from app.core.redis import get_redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = get_redis()
    await redis.ping()
    print("redis works")
    yield
    await redis.aclose()
    print("redis turned off")

app = FastAPI(lifespan=lifespan)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
def health():
    return {"ok": True}

