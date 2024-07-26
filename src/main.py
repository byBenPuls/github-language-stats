from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.responses import HTMLResponse, RedirectResponse

from src.database.caching import redis
from src.svg.card import UserData
from src.svg.themes import themes


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Creating connection to databases at startup and their closing at turning off
    :param app:
    """
    await redis.create_connection()
    yield
    await redis.close_connection()


app = FastAPI(lifespan=lifespan)


@app.get('/')
async def main_page(username: str = None, theme: str = None):
    """
    Main page
    :param theme: Card background theme
    :param username: GitHub username
    :return:
    """
    if theme not in themes:
        theme = 'main'

    if username is None:
        return RedirectResponse('https://github.com/byBenPuls')
    card = await UserData(username, theme).card()
    return HTMLResponse(content=card, status_code=200, media_type='image/svg+xml')
