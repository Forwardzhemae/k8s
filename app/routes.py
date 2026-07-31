from fastapi import APIRouter
from app.api.gamers import router as gamers_router

api_router = APIRouter(prefix="/api")
api_router.include_router(gamers_router)
