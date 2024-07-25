import time

from src.database.redis import RedisPool

redis = RedisPool()


async def in_cache(key: str) -> bool:
    conn = await redis.get_connection()
    return bool(await conn.lrange(key, 0, -1))


async def record_in_cache(key: str, *values) -> None:
    conn = await redis.get_connection()
    await conn.lpush(key, *values)
    await conn.expireat(key, int(time.time()) + 60 * 60)


async def get_from_cache(key: str) -> list:
    conn = await redis.get_connection()
    values = [i.decode('utf-8') for i in (await conn.lrange(key, 0, -1))[::-1]]

    return values
