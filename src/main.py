from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.responses import HTMLResponse, RedirectResponse

from src.database.caching import redis
from src.svg.card import UserData
from src.svg import themes


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Creating connection to databases at startup and their closing at turning off
    :param app:
    """
    await redis.create_connection()
    yield
    await redis.close_connection()

# TODO: создавать приложение через фабрикеу (вкусовщина)
app = FastAPI(lifespan=lifespan)

# TODO: хендлеры в отдельном файле (вкусовщина)
# TODO: type hint str | None или нормальный default поставить что бы не обрабатывать None
@app.get('/')
async def main_page(username: str | None = None, theme: str = 'main') -> HTMLResponse | RedirectResponse: 
    # TODO: обчыно так не делают. Импортят Query и пишут descriprion там. 
    # TODO: Так же как и с возвратным значением. В свагер автоматом подтянется
    """
    Main page
    :param theme: Card background theme
    :param username: GitHub username
    """
    if theme not in themes:
        theme = 'main'

    if username is None:
        return RedirectResponse('https://github.com/byBenPuls')
    # TODO: у тебя обработка логики и сборка свг файла происходит в одном месте. Надо делить
    # cart = await GetLangCart().execute(username)
    # cart_svg = CartSVGBuilder().build()
    card = await UserData(username, theme).card()
    return HTMLResponse(content=card, status_code=200, media_type='image/svg+xml')
