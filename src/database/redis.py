import logging
import pickle

import redis.asyncio as redis

from src.settings import settings

logger = logging.getLogger("uvicorn.info")


class Redis:
    def __init__(self) -> None:
        logger.info("Redis initialized!")
        client = redis.ConnectionPool(
            host=settings.REDIS_HOST,
            port=int(settings.REDIS_PORT),
            db=int(settings.REDIS_DB),
            password=settings.REDIS_PASSWORD,
        )
        self.pool = redis.Redis.from_pool(connection_pool=client)

    async def in_cache(self, key: str) -> bool:
        return bool(await self.pool.get(key))

    async def get_from_cache(self, key: str) -> dict | None:
        if value := await self.pool.get(key):
            return pickle.loads(value)
        return value

    async def record_in_cache(self, key: str, value: dict, ex: int = 3600) -> None:
        value = pickle.dumps(value)
        await self.pool.set(key, value, ex=ex)

    async def close_connection(self) -> None:
        await self.pool.aclose()
