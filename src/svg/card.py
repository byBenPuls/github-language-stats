import json
from xml.etree import ElementTree as Et

from src.exceptions import NotFoundUserError, RequestLimitError
from src.github.api import get_languages_stats_from_repos
from src.svg.language import languages_group, create_language, custom_data_text
from src.svg import *


def get_colors():
    with open('src/colors.json', 'r') as file:
        colors = json.load(file)
    return colors


data = get_colors()


def create_svg(theme_name: str, *elements):
    theme_class = themes.get(theme_name, Main)
    return Et.tostring(theme_class(*elements).card())


class UserData:
    def __init__(self, username: str,
                 theme_name: str):
        self.username = username
        self.theme_name = theme_name

    async def card(self):
        try:
            languages = await get_languages_stats_from_repos(self.username)
        except (NotFoundUserError, RequestLimitError) as e:
            return create_svg(self.theme_name,
                              *languages_group(create_language(name=None, color=None,
                                                               special_message=custom_data_text(
                                                                   e.message))))
        # if not languages:
        #     return create_svg(css(), custom_data_text('No languages found'))
        lang_list = [create_language(i, data[i]['color']) for i in languages]
        if not lang_list:
            lang_list = [create_language(name=None, color=None,
                                         special_message=custom_data_text('No languages found'))]
        return create_svg(self.theme_name, *languages_group(*lang_list))
