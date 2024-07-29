import logging
import typing

import redis.asyncio as redis

# TODO все логгеры можно сделать logging.getLogger(__name__)
logger = logging.getLogger("uvicorn.info")


class RedisPool:
    def __init__(self) -> None:
        self.pool = None

    async def create_connection(self) -> None:
        # TODO не понятно зачем асинхронный
        # TODO я думаю это можно в конструктор
        logger.info('Trying to connect..')
        client = redis.ConnectionPool()
        self.pool = redis.Redis.from_pool(client)
        logger.info('Successfully connected!')

    async def get_connection(self) -> typing.Optional[redis.Redis]:
        # TODO не понятно зачем асинхронный
        # TODO не понятно зачем вообще)
        return self.pool

    async def close_connection(self):
        await self.pool.aclose()
