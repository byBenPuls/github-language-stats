from xml.etree import ElementTree as Et

from src.svg.css import CssBuilder


def generate_css(
    header_fill: str = "#2f80ed",
    lang_name_fill: str = "#434d58",
    stat_fill: str = "#434d58",
):
    css_styles = {
        "#header": {
            "font": "600 18px 'Segoe UI', Ubuntu, Sans-Serif",
            "fill": header_fill,
            "animation": "fadeInAnimation 0.8s ease-in-out forwards",
        },
        "#lang-name": {
            "font": "500 12px 'Segoe UI', Ubuntu, Sans-Serif",
            "fill": lang_name_fill,
        },
        "#bold": {"font-weight": "700"},
        "#stat": {
            "font": "700 16px 'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif",
            "fill": stat_fill,
            "animation": "fadeInAnimation 0.5s ease-in-out forwards",
        },
        "#stagger": {
            "opacity": "0",
            "animation": "fadeInAnimation 0.3s ease-in-out forwards",
        },
        "@supports(-moz-appearance: auto)": {
            ".header": {"font-size": "15.5px"},
            "#stat": {"font-size": "13px"},
        },
        "@keyframes fadeInAnimation": {
            "from": {"opacity": "0"},
            "to": {"opacity": "1"},
        },
    }

    return CssBuilder(css_styles).build()


def background(
    x: str = "0.5",
    y: str = "0.5",
    rx: str = "4.5",
    height: str = "99",
    stroke: str = "#e4e2e2",
    width: str = "299",
    fill: str = "#fffefe",
    attrib=None,
):
    if attrib is None:
        attrib = {}
    return Et.Element(
        "rect",
        xmlns="http://www.w3.org/2000/svg",
        x=x,
        y=y,
        rx=rx,
        height=f"{height}%",
        stroke=stroke,
        width=width,
        fill=fill,
        attrib=attrib,
    )


class BaseTheme:
    def __init__(self, width: str):
        self.width = str(int(width) - 1)
        self.root = []

    def insert_css_text_colors(self):
        self.root.append(
            generate_css(
                header_fill="#2f80ed", lang_name_fill="#434d58", stat_fill="#434d58"
            )
        )
        self.root.append(background(width=self.width))

    def card(self):
        self.insert_css_text_colors()
        return self.root


class GradientGenerator:
    def __init__(self, rotate: int = 30, *gradient_colors: tuple[int, str]) -> None:
        self.rotate = rotate
        self.gradient_colors = gradient_colors

    def generate(self):
        defs = Et.Element("defs", xmlns="http://www.w3.org/2000/svg")
        gradient = Et.Element(
            "linearGradient",
            id="gradient",
            gradientTransform="rotate({})".format(self.rotate),
            gradientUnits="userSpaceOnUse",
        )
        defs.append(gradient)
        for offset, stop_color in self.gradient_colors:
            stop = Et.Element(
                "stop", offset="{}%".format(offset), attrib={"stop-color": stop_color}
            )
            gradient.append(stop)
        return defs


class Main(BaseTheme):
    def __init__(self, width) -> None:
        super().__init__(width)
        self.root.append(generate_css())


class Gradient(BaseTheme):
    def __init__(self, width) -> None:
        super().__init__(width)
        self.root.append(
            generate_css(header_fill="#fff", lang_name_fill="#fff", stat_fill="#fff")
        )

    def insert_css_text_colors(self):
        self.root.append(
            GradientGenerator(0, (5, "#e96443"), (95, "#904e95")).generate()
        )
        self.root.append(
            background(
                width=self.width, fill="url(#gradient)", attrib={"stroke-opacity": "1"}
            )
        )


class Dark(BaseTheme):
    def __init__(self, width) -> None:
        super().__init__(width)
        self.root.append(
            generate_css(
                header_fill="#58A6FF", lang_name_fill="#C3D1D9", stat_fill="#C3D1D9"
            )
        )

    def insert_css_text_colors(self):
        self.root.append(
            background(width=self.width, fill="#0D1117", attrib={"stroke-opacity": "1"})
        )


class Monokai(BaseTheme):
    def __init__(self, width):
        super().__init__(width)
        self.root.append(
            generate_css(
                header_fill="#eb1f6a", lang_name_fill="#DEE2E4", stat_fill="#DEE2E4"
            )
        )

    def insert_css_text_colors(self):
        self.root.append(
            background(width=self.width, fill="#272822", attrib={"stroke-opacity": "1"})
        )


class AmbientGradient(BaseTheme):
    def __init__(self, width):
        super().__init__(width)
        self.root.append(
            generate_css(header_fill="#fff", lang_name_fill="#fff", stat_fill="#fff")
        )

    def insert_css_text_colors(self):
        gradient = GradientGenerator(
            35, (0, "#4158d0"), (50, "#c850c0"), (100, "#ffcc70")
        ).generate()
        self.root.append(gradient)
        self.root.append(
            background(
                width=self.width, fill="url(#gradient)", attrib={"stroke-opacity": "1"}
            )
        )


# TODO много дублирующего кода
class OceanBlueGradient(BaseTheme):
    def __init__(self, width):
        super().__init__(width)
        self.root.append(
            generate_css(header_fill="#fff", lang_name_fill="#fff", stat_fill="#fff")
        )

    def insert_css_text_colors(self):
        gradient = GradientGenerator(35, (0, "#2E3192"), (100, "#1BFFFF")).generate()
        self.root.append(gradient)
        self.root.append(
            background(
                width=self.width, fill="url(#gradient)", attrib={"stroke-opacity": "1"}
            )
        )


class EternalConstanceGradient(BaseTheme):
    def __init__(self, width):
        super().__init__(width)
        self.root.append(
            generate_css(header_fill="#fff", lang_name_fill="#fff", stat_fill="#fff")
        )

    def insert_css_text_colors(self):
        gradient = GradientGenerator(0, (5, "#09203F"), (95, "#537895")).generate()
        self.root.append(gradient)
        self.root.append(
            background(
                width=self.width, fill="url(#gradient)", attrib={"stroke-opacity": "1"}
            )
        )


class ViceCityGradient(BaseTheme):
    def __init__(self, width):
        super().__init__(width)
        self.root.append(
            generate_css(header_fill="#fff", lang_name_fill="#fff", stat_fill="#fff")
        )

    def insert_css_text_colors(self):
        gradient = GradientGenerator(0, (5, "#3494e6"), (95, "#ec6ead")).generate()
        self.root.append(gradient)
        self.root.append(
            background(
                width=self.width, fill="url(#gradient)", attrib={"stroke-opacity": "1"}
            )
        )


class PurpinkGradient(BaseTheme):
    def __init__(self, width):
        super().__init__(width)
        self.root.append(
            generate_css(header_fill="#fff", lang_name_fill="#fff", stat_fill="#fff")
        )

    def insert_css_text_colors(self):
        gradient = GradientGenerator(0, (5, "#7f00ff"), (95, "#e100ff")).generate()
        self.root.append(gradient)
        self.root.append(
            background(
                width=self.width, fill="url(#gradient)", attrib={"stroke-opacity": "1"}
            )
        )
