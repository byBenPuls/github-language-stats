import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.github.api import get_languages_stats_from_repos
from src.database.caching import redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Creating connection to databases at startup and their closing at turning off
    :param app:
    """
    await redis.create_connection()
    yield
    await redis.close_connection()


class Item(BaseModel):
    languages: bool


app = FastAPI(lifespan=lifespan)
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/src/static", StaticFiles(directory=static_dir, html=True), name="static")

templates = Jinja2Templates(directory='src/static')

from src.svg.card import UserData


@app.get('/')
async def main_page(username: str = None):
    if username is None:
        return RedirectResponse('https://github.com/byBenPuls')
    card = await UserData(username).card()
    return HTMLResponse(content=card, status_code=200, media_type='image/svg+xml')

    # return templates.TemplateResponse('index.html',
    #                                   media_type='image/svg+xml', context={'request': request})


@app.post('/')
async def languages(item: Item):
    return {'response': await get_languages_stats_from_repos('byBenPuls')}
