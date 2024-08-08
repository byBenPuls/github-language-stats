from src.svg.elements import Element, Group


class LanguagesGroup:
    def __init__(self, columns, *languages: Element) -> None:
        self.languages = languages
        self.columns = columns

    @staticmethod
    def header() -> Element:
        el_header = Element(
            tag="text",
            attrib={"text-align": "center"},
            x="0%",
            y="0%",
            fill="black",
            id="header",
        )
        el_header.text = "Most Used Languages"
        return el_header

    @staticmethod
    def form_group(language: Element, x: int, y: int, animation_delay: int) -> Element:
        return Group(
            Group(language, transform=f"translate({x}, {y})"),
            id="stagger",
            style=f"animation-delay: {animation_delay}ms",
        )

    def langs(self) -> list[Element]:
        svg = []

        animation_delay, t_x, t_y = 450, 0, 0
        iterations, columns = 0, 1
        for language in self.languages:
            iterations += 1
            if iterations > 3:
                if columns > self.columns:
                    break
                iterations, animation_delay = 1, 450
                columns += 1
                t_x += 150
                t_y = 0
            svg.append(self.form_group(language, t_x, t_y, animation_delay))

            t_y += 25
            animation_delay += 150
        return svg

    def build(self) -> Element:
        languages = self.langs()
        return Group(
            Group(self.header(), transform="translate(25, 35)"),
            Group(
                Element(*languages, tag="svg", x="25"),
                transform="translate(0, 55)",
            ),
            transform="translate(0, 0)",
        )


class LanguageLabel:
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def label(self) -> Element:
        element = Element(tag="text", x="15", y="10", fill="black", id="lang-name")
        element.text = self.name
        return element

    def circle(self) -> Element:
        element = Element(tag="circle", cx="5", cy="6", fill=self.color, r="5")
        return element

    def build(self) -> Element:
        return Group(self.circle(), self.label())


def custom_data_text(msg: str) -> Element:
    message = Element(
        tag="text",
        attrib={"text-anchor": "middle", "dominant-baseline": "middle"},
        x="50%",
        y="50%",
        fill="#434d58",
        id="stat",
    )
    message.text = msg
    return message
