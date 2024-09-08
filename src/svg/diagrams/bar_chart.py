from src.svg.elements import Element, Group
from src.constants import COLORS
from src.svg.language import LanguageLabel


class Column:
    def __init__(
        self, x: int | str, y: int | str, width: int | str, height: int | str, fill: str
    ) -> None:
        self.x = str(x)
        self.y = str(y)
        self.width = str(width)
        self.height = str(height)
        self.fill = fill

    def render(self) -> Element:
        return Element(
            tag="rect",
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            fill=self.fill,
            rx="3",
        )


class BarChartLegend:
    def __init__(self, languages: dict[str, int | float]) -> None:
        self.languages = languages

    def create_a_language_labels(self):
        return (
            LanguageLabel(k, COLORS[k]["color"]).build() for k in self.languages.keys()
        )

    def transform_a_language_labels(self):
        group = []

        count_of_languages_in_a_row = 0
        counter = 0
        for lang in self.create_a_language_labels():
            counter += 1
            if counter > 3:
                counter = 1
                count_of_languages_in_a_row += 1
            group.append(
                Group(
                    lang,
                    transform=f"translate({count_of_languages_in_a_row * 100}, {counter * 20})",
                )
            )

        return group

    def group_a_language_labels(self):
        return Group(*self.transform_a_language_labels())

    def build(self) -> Element:
        return Group(self.group_a_language_labels())


class BarChartDiagram:
    def __init__(self, languages: dict[str, int | float]) -> None:
        self.languages = languages
        self.summary_languages_usage = sum(languages.values())
        langs = {
            k: {
                "percentage": (v / self.summary_languages_usage * 100),
                "color": COLORS[k]["color"],
            }
            for k, v in languages.items()
        }

        self.svg_columns = (
            Column(
                x * 15,
                f"{100 - langs[k]["percentage"]}%",
                "10",
                f"{langs[k]["percentage"]}%",
                langs[k]["color"],
            ).render()
            for x, k in enumerate(langs)
        )

    def build_a_chart_legend(self):
        return BarChartLegend(self.languages).build()

    def build(self) -> Element:
        return Group(*self.svg_columns, self.build_a_chart_legend())
