from src.svg.elements import Element, Group


class LanguagesGroup:
    def __init__(self, columns: int, *languages: Element) -> None:
        self.languages = languages
        self.columns = columns

    @staticmethod
    def create_header() -> Element:
        header = Element(
            tag="text",
            attrib={"text-align": "center"},
            x="0%",
            y="0%",
            fill="black",
            id="header",
        )
        header.text = "Most Used Languages"
        return header

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
            Group(self.create_header(), transform="translate(25, 35)"),
            Group(
                Element(*languages, tag="svg", x="25"),
                transform="translate(0, 55)",
            ),
            transform="translate(0, 0)",
        )
