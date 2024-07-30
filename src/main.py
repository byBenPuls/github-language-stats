from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.redis import Redis
from src.api.routers import router


async def get_db():
    redis = Redis()
    try:
        yield redis.pool
    finally:
        await redis.pool.aclose()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Creating connection to databases at startup and their closing at turning off
    :param app:
    """
    await redis.create_connection()
    yield
    await redis.close_connection()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    return app
