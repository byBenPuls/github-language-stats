from xml.etree import ElementTree as Et


def header():
    header_element = Et.Element("text", x="0", y="0", fill="black", id="header")
    header_element.text = "Most Used Languages"
    return header_element


class Group:
    def __init__(self, attrib: dict[str, str] = {}, **extra: str) -> None:
        self.attrib = attrib
        self.extra = extra

    def build(self, *elements):
        self.root = Et.Element("g", attrib=self.attrib, **self.extra)
        for element in elements:
            self.root.append(element)
        return self.root


class LanguagesList:
    def __init__(self, limit: int, *languages: Et.Element) -> None:
        self.languages = languages
        self.limit = limit

    def create(self):
        root = Et.Element("g", transform="translate(0, 0)")

        header_g = Et.Element("g", transform="translate(25, 35)")
        root.append(header_g)

        header_g.append(header())

        main_g = Et.Element("g", transform="translate(0, 55)")
        root.append(main_g)

        svg_ = Et.Element("svg", x="25")
        main_g.append(svg_)

        animation_delay = 450
        t_x, t_y = 0, 0
        count = 0
        for count, language in enumerate(self.languages, start=1):
            if count == self.limit:
                return root
            g_animation = Et.Element(
                "g", id="stagger", style=f"animation-delay: {animation_delay}ms"
            )
            language_group = Et.Element("g", transform=f"translate({t_x}, {t_y})")
            g_animation.append(language_group)
            language_group.append(language)
            svg_.append(g_animation)

            t_y += 25
            animation_delay += 150


class Languages:
    def __init__(self, columns, *languages: Et.Element) -> None:
        self.languages = languages
        self.columns = columns

    def group(self, columns: int = 2) -> Et.Element:
        root = Et.Element("g", transform="translate(0, 0)")

        header_g = Et.Element("g", transform="translate(25, 35)")
        root.append(header_g)

        header_g.append(header())

        main_g = Et.Element("g", transform="translate(0, 55)")
        root.append(main_g)

        svg_ = Et.Element("svg", x="25")
        main_g.append(svg_)

        animation_delay = 450
        t_x, t_y = 0, 0
        count = 0
        column_count = 1
        for language in self.languages:
            count += 1
            if count > 3:
                if column_count > self.columns:
                    return root
                count = 1
                column_count += 1
                animation_delay = 450
                t_x += 150
                t_y = 0

            g_animation = Et.Element(
                "g", id="stagger", style=f"animation-delay: {animation_delay}ms"
            )
            language_group = Et.Element("g", transform=f"translate({t_x}, {t_y})")
            g_animation.append(language_group)
            language_group.append(language)
            svg_.append(g_animation)

            t_y += 25
            animation_delay += 150
        return root


def create_language(
    name: str | None = None,
    color: str | None = None,
    special_message: Et.Element | None = None,
):
    if name is None and color is None:
        return special_message

    def language_name():
        element = Et.Element("text", x="15", y="10", fill="black", id="lang-name")
        element.text = name
        return element

    root = Et.Element("g")

    root.append(Et.Element("circle", cx="5", cy="6", fill=color, r="5"))
    root.append(language_name())

    return root


def elements_group(*languages):
    root = Et.Element("g", transform="translate(0, 0)")

    header_g = Et.Element("g", transform="translate(25, 35)")
    root.append(header_g)

    header_g.append(header())

    main_g = Et.Element("g", transform="translate(0, 55)")
    root.append(main_g)

    svg_ = Et.Element("svg", x="25")
    main_g.append(svg_)

    animation_delay = 450
    t_x, t_y = 0, 0
    for count, language in enumerate(languages, start=1):
        if count == 4:
            animation_delay = 450
            t_x, t_y = 150, 0

        g_animation = Et.Element(
            "g", id="stagger", style=f"animation-delay: {animation_delay}ms"
        )
        language_group = Et.Element("g", transform=f"translate({t_x}, {t_y})")
        g_animation.append(language_group)
        language_group.append(language)
        svg_.append(g_animation)

        t_y += 25
        animation_delay += 150
    return root


def custom_data_text(msg: str):
    message = Et.Element("text", x="0", y="11", fill="#434d58", id="stat")
    message.text = msg
    return message
