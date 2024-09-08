import logging
from xml.etree import ElementTree as Et

from src.constants import COLORS
from src.svg import themes, Main
from src.svg.elements import Element
from src.svg.diagrams.list import LanguagesGroup
from src.svg.language import LanguageLabel
from src.svg.utils import create_custom_data_text

logger = logging.getLogger("uvicorn.info")


class ComposeCard:
    def __init__(self, theme, count_columns: int = 2) -> None:
        self.theme = theme
        self.columns = count_columns

    def _render(
        self, width: str, height: str, view_box: str, *elements: Element
    ) -> bytes:
        theme_elements = (i for i in self.theme(width=width).card())
        root = Element(
            *theme_elements,
            *elements,
            tag="svg",
            xmlns="http://www.w3.org/2000/svg",
            width=width,
            height=height,
            viewBox=view_box,
            fill="none",
            role="img",
        ).render()
        return Et.tostring(root)

    def visualize(self, *languages_data: Et.Element) -> bytes:
        width = 150 * self.columns
        return self._render(str(width), "140", f"0 0 {width} 140", *languages_data)


class UserCard:
    def __init__(
        self,
        languages: dict,
        theme_name: str,
        columns: int,
        exception: Exception | None = None,
    ) -> None:
        self.languages = list(languages.keys())
        self.theme_name = themes.get(theme_name, Main)
        self.columns = columns
        self.exception = exception

    async def card(self) -> bytes:
        lang_list = tuple(
            LanguageLabel(lang, COLORS[lang]["color"]).build()
            for lang in self.languages
        )
        main_card = ComposeCard(theme=self.theme_name, count_columns=self.columns)
        user_has_languages = len(lang_list)

        if self.exception:
            logger.error(self.exception)
            return main_card.visualize(create_custom_data_text(str(self.exception)))
        if not user_has_languages:
            logger.warning("Languages not found")
            return main_card.visualize(create_custom_data_text("No languages found :("))
        return main_card.visualize(LanguagesGroup(self.columns, *lang_list).build())
