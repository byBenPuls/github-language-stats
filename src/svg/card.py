import logging
from xml.etree import ElementTree as Et

from src.constants import COLORS
from src.svg import themes, Main
from src.svg.language import (
    create_language,
    custom_data_text,
    Languages,
)

logger = logging.getLogger("uvicorn.info")


class CreateCard:
    def __init__(self, theme, count_columns: int = 2) -> None:
        self.theme = theme
        self.columns = count_columns

    def __render(self, width, height, view_box, *elements):
        root = Et.Element(
            "svg",
            xmlns="http://www.w3.org/2000/svg",
            width=width,
            height=height,
            viewBox=view_box,
            fill="none",
            role="img",
        )
        for i in self.theme(width=width).card():
            logger.info(i)
            root.append(i)
        for i in elements:
            root.append(i)
        return Et.tostring(root)

    def compact_style(self, *languages_data: Et.Element):
        width = 150 * self.columns
        return self.__render(str(width), "140", f"0 0 {width} 140", *languages_data)

    def donut(self, *languages_data: Et.Element):
        return self.__render("450", "140", "0 0 450 140", *languages_data)


class UserData:
    def __init__(self, languages: dict, theme_name: str, columns: int):
        self.languages = list(languages.keys())
        self.theme_name = themes.get(theme_name, Main)
        self.columns = columns
        logger.info(self.languages)

    async def card(self):
        # return CreateCard(theme=self.theme_name).compact_style(
        #     *elements_group(create_language(name=None, color=None,
        #                                     special_message=custom_data_text(
        #                                         e.message))))
        lang_list = [create_language(i, COLORS[i]["color"]) for i in self.languages]
        main_card = CreateCard(theme=self.theme_name, count_columns=self.columns)

        if not lang_list:
            return main_card.compact_style(custom_data_text("No languages found :("))
        return main_card.compact_style(
            Languages(self.columns, *lang_list).group(columns=self.columns)
        )
