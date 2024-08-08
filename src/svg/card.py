import logging
from xml.etree import ElementTree as Et

from src.constants import COLORS
from src.svg import themes, Main
from src.svg.elements import Element
from src.svg.language import (
    LanguageLabel,
    custom_data_text,
    LanguagesGroup,
)

logger = logging.getLogger("uvicorn.info")


class ComposeCard:
    def __init__(self, theme, count_columns: int = 2) -> None:
        self.theme = theme
        self.columns = count_columns

    def __render(
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
        return self.__render(str(width), "140", f"0 0 {width} 140", *languages_data)


class UserData:
    def __init__(self, languages: dict, theme_name: str, columns: int) -> None:
        self.languages = list(languages.keys())
        self.theme_name = themes.get(theme_name, Main)
        self.columns = columns
        logger.info(self.languages)

    async def card(self) -> bytes:
        lang_list = [
            LanguageLabel(lang, COLORS[lang]["color"]).build()
            for lang in self.languages
        ]
        main_card = ComposeCard(theme=self.theme_name, count_columns=self.columns)

        if not lang_list:
            return main_card.visualize(custom_data_text("No languages found :("))
        return main_card.visualize(
            LanguagesGroup(self.columns, *lang_list).build()
        )
