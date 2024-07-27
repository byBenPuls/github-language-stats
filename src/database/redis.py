import logging
import typing

import redis.asyncio as redis

logger = logging.getLogger("uvicorn.error")


class RedisPool:
    def __init__(self) -> None:
        self.pool = None

    async def create_connection(self) -> None:
        logger.debug('Trying to connect..')
        client = redis.ConnectionPool()
        self.pool = redis.Redis.from_pool(client)
        logger.debug('Successfully connected!')

    async def get_connection(self) -> typing.Optional[redis.Redis]:
        return self.pool

    async def close_connection(self):
        await self.pool.aclose()
