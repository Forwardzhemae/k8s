import json
from sqlalchemy import select

from app.core.redis import get_redis
from app.models.gamers import Gamer


async def get_gamers_with_cache(session):
    redis = get_redis()
    key = "gamers:all"

    cached = await redis.get(key)

    if cached:
        return json.loads(cached)

    result = await session.execute(select(Gamer))
    gamers = result.scalars().all()

    gamers_data = [
        {
        "id": gamer.id,
        "name": gamer.name,
        "sec_name": gamer.sec_name,
        "email": gamer.email,
        "game_name": gamer.game_name,
        }
        for gamer in gamers
    ]
    await redis.set(key, json.dumps(gamers_data), ex=60)

    return gamers_data
