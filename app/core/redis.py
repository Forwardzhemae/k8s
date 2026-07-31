from redis.asyncio import Redis
from functools import lru_cache


@lru_cache()
def get_redis() -> Redis:
    return Redis(host="redis", port=6379)
