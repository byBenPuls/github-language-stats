from xml.etree import ElementTree as Et

from src.github.api import get_languages_stats_from_repos
from src.svg.language import languages_group, create_language, no_language_data

import json


def get_colors():
    with open('src/static/colors.json', 'r') as file:
        colors = json.load(file)
    return colors


data = get_colors()


def css():
    style = Et.Element('style')
    style.text = """
    #header {
            font: 600 18px 'Segoe UI', Ubuntu, Sans-Serif;
            fill: #2f80ed;
            animation: fadeInAnimation 0.8s ease-in-out forwards;
    }
    
    #lang-name {
        font: 400 11px "Segoe UI", Ubuntu, Sans-Serif;
        fill: #434d58;
    }
    
    #bold {
        font-weight: 700;
    }
    
    #stat {
        font: 700 14px 'Segoe UI', Ubuntu, "Helvetica Neue", Sans-Serif;
        fill: #434d58;
    }
    
    #stagger {
        opacity: 0;
        animation: fadeInAnimation 0.3s ease-in-out forwards;
    }
    
    @keyframes fadeInAnimation {
        from {
        opacity: 0;
        }
        to {
        opacity: 1;
        }
    }
    """

    return style


def create_svg(*elements):
    root = Et.Element("svg", xmlns="http://www.w3.org/2000/svg", width="300",
                      height="140", viewBox="0 0 300 140", fill="none", role="img")

    rect = Et.Element('rect', x='0.5', y='0.5',
                      rx="4.5", height="99%", stroke="#e4e2e2",
                      width="299", fill="#fffefe")
    root.append(rect)
    for i in elements:
        root.append(i)

    return Et.tostring(root)


class UserData:
    def __init__(self, username):
        self.username = username

    async def languages(self):
        return await get_languages_stats_from_repos(self.username)

    async def card(self):
        languages = await self.languages()
        if not languages:
            return create_svg(css(), no_language_data())
        lang_list = [create_language(i, data[i]['color']) for i in languages]

        return create_svg(css(), *languages_group(*lang_list))
