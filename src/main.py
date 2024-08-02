from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.routers import router
from src.container import get_container
from src.database.redis import Redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Creating connection to databases at startup and their closing at turning off
    :param app:
    """
    redis = get_container().resolve(Redis)
    yield
    await redis.close_connection()


def create_app() -> FastAPI:
    """
    Factory FastAPI
    """
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    return app
