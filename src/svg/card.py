import logging
from xml.etree import ElementTree as Et

from src.constants import COLORS
from src.svg import themes, Main
from src.svg.language import elements_group, create_language, custom_data_text

logger = logging.getLogger("uvicorn.info")


class CreateCard:
    def __init__(self, theme) -> None:
        self.theme = theme

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
        return self.__render("300", "140", "0 0 300 140", *languages_data)

    def donut(self, *languages_data: Et.Element):
        return self.__render("350", "215", "0 0 350 215", *languages_data)


class UserData:
    def __init__(self, languages: dict, theme_name: str):
        self.languages = list(languages.keys())
        self.theme_name = themes.get(theme_name, Main)
        logger.info(self.languages)

    async def card(self):
        # return CreateCard(theme=self.theme_name).compact_style(
        #     *elements_group(create_language(name=None, color=None,
        #                                     special_message=custom_data_text(
        #                                         e.message))))
        lang_list = [create_language(i, COLORS[i]["color"]) for i in self.languages]
        if not lang_list:
            lang_list = [
                create_language(special_message=custom_data_text("No languages found"))
            ]
        return CreateCard(theme=self.theme_name).compact_style(*elements_group(*lang_list))
