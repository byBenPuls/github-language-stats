from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import Response, RedirectResponse, HTMLResponse

from src.svg import themes
from src.svg.card import UserData

router = APIRouter()


@router.get('/')
async def main_page(username: str | None = None, theme: str = 'main') -> Response:
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
    return HTMLResponse(content=card, status_code=HTTPStatus.OK, media_type='image/svg+xml')
