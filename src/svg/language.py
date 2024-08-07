import logging
from xml.etree import ElementTree as Et
from src.svg.elements import Element, Group

logger = logging.getLogger("uvicorn.info")


def header():
    el_header = Element(
        tag="text",
        attrib={"text-align": "center"},
        x="0%",
        y="0%",
        fill="black",
        id="header",
    )
    el_header.text = "Most Used Languages"
    logger.info(el_header)
    return el_header


class Languages:
    def __init__(self, columns, *languages: Et.Element) -> None:
        self.languages = languages
        self.columns = columns

    def langs(self):
        svg = []

        animation_delay = 450
        t_x, t_y = 0, 0
        count = 0
        column_count = 1
        for language in self.languages:
            count += 1
            if count > 3:
                if column_count > self.columns:
                    break
                count = 1
                column_count += 1
                animation_delay = 450
                t_x += 150
                t_y = 0

            g_animation = Group(
                Group(language, transform=f"translate({t_x}, {t_y})"),
                id="stagger",
                style=f"animation-delay: {animation_delay}ms",
            )
            svg.append(g_animation)

            t_y += 25
            animation_delay += 150
        return svg

    def group(self, columns: int = 2) -> Et.Element:
        lst = self.langs()
        root = Group(
            Group(header(), transform="translate(25, 35)"),
            Group(
                Element(*lst, tag="svg", x="25"),
                transform="translate(0, 55)",
            ),
            transform="translate(0, 0)",
        )
        logger.info(root)
        return root.render()


def create_language(
    name: str,
    color: str,
):
    def language_name():
        element = Element(tag="text", x="15", y="10", fill="black", id="lang-name")
        element.text = name
        return element

    root = Group(
        Element(tag="circle", cx="5", cy="6", fill=color, r="5"), language_name()
    )
    return root


def custom_data_text(msg: str):
    message = Element(
        tag="text",
        attrib={"text-anchor": "middle", "dominant-baseline": "middle"},
        x="50%",
        y="50%",
        fill="#434d58",
        id="stat",
    )
    message.text = msg
    return message.render()
