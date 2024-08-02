from http import HTTPStatus

from fastapi import APIRouter, Depends, Query
from starlette.responses import Response, RedirectResponse, HTMLResponse

from src.container import get_container
from src.database.redis import Redis
from src.svg import themes
from src.svg.card import UserData
from src.database.caching import CachedProgramLangRepo
from src.github.repos import ProgramLangRepo

router = APIRouter()


def get_db():
    return get_container().resolve(Redis)


@router.get("/", description="Returns SVG card with programming languages stats")
async def main_page(
    username: str | None = Query(
        default=None,
        description="Github username. If not set, redirects to https://github.com/byBenPuls",
    ),
    theme: str = Query(
        title="Theme",
        default="main",
        description="Background theme name",
        examples=list(themes.keys()),
    ),
    columns: int | None = None,
    lang_list: int | None = None
    db=Depends(get_db),
) -> Response:
    if theme not in themes:
        theme = "main"

    if username is None:
        return RedirectResponse("https://github.com/byBenPuls")
    # TODO: у тебя обработка логики и сборка свг файла происходит в одном месте. Надо делить
    # cart = await GetLangCart().execute(username)
    languages = await CachedProgramLangRepo(db, ProgramLangRepo()).fetch_lang(
        username, 99
    )
    # cart_svg = CartSVGBuilder().build()
    if columns is not None:
        columns = 2 if columns < 2 else columns
        card = await UserData(languages, theme, columns).card()
        return HTMLResponse(
        content=card, status_code=HTTPStatus.OK, media_type="image/svg+xml"
        )
