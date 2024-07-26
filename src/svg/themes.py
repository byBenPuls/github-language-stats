from xml.etree import ElementTree as Et


def css(header_fill: str = '#2f80ed',
        lang_name_fill: str = '#434d58',
        stat_fill: str = '#434d58'):
    style = Et.Element('style')
    style.text = """
    #header {
            font: 600 18px 'Segoe UI', Ubuntu, Sans-Serif;
            fill: """ + header_fill + """;
            animation: fadeInAnimation 0.8s ease-in-out forwards;
    }
    
    @supports(-moz-appearance: auto) {
            .header { font-size: 15.5px; }
    }

    #lang-name {
        font: 500 12px "Segoe UI", Ubuntu, Sans-Serif;
        fill: """ + lang_name_fill + """;
    }

    #bold {
        font-weight: 700;
    }

    #stat {
        font: 700 14px 'Segoe UI', Ubuntu, "Helvetica Neue", Sans-Serif;
        fill: """ + stat_fill + """;
    }
    
     @supports(-moz-appearance: auto) {
      #stat { font-size:13px; }
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


class BaseTheme:
    def __init__(self, *elements):
        self.elements = elements
        self.root = Et.Element("svg", xmlns="http://www.w3.org/2000/svg", width="300",
                               height="140", viewBox="0 0 300 140", fill="none", role="img")
        self.root.append(css(
            header_fill='#fff',
            lang_name_fill='#fff',
            stat_fill='#fff'
        ))

    def background(self):
        raise NotImplementedError

    def insert(self):
        for i in self.elements:
            self.root.append(i)

    def card(self):
        self.background()
        self.insert()
        return self.root


class GradientGenerator:
    def __init__(self, rotate: int = 30,
                 *gradient_colors: tuple[int, str]) -> None:
        self.rotate = rotate
        self.gradient_colors = gradient_colors

    def generate(self):
        defs = Et.Element('defs', xmlns="http://www.w3.org/2000/svg")
        gradient = Et.Element('linearGradient', id="gradient",
                              gradientTransform="rotate({})".format(self.rotate),
                              gradientUnits="userSpaceOnUse")
        defs.append(gradient)
        for i in self.gradient_colors:
            stop = Et.Element('stop', offset="{}%".format(i[0]), attrib={'stop-color': i[1]})
            gradient.append(stop)
        return defs


class MainTheme(BaseTheme):
    def __init__(self, *elements) -> None:
        super().__init__(*elements)
        self.root.append(css())

    def background(self):
        rect = Et.Element('rect', x='0.5', y='0.5',
                          rx="4.5", height="99%", stroke="#e4e2e2",
                          width="299", fill="#fffefe")

        self.root.append(rect)


class GradientTheme(BaseTheme):
    def background(self):
        defs = Et.Element('defs', xmlns="http://www.w3.org/2000/svg")
        self.root.append(defs)
        linear_gradient = Et.Element('linearGradient', id="gradient", gradientTransform="rotate(30)",
                                     gradientUnits="userSpaceOnUse")
        defs.append(linear_gradient)
        stop1 = Et.Element('stop', offset="0%", attrib={'stop-color': "#e96443"})
        stop2 = Et.Element('stop', offset="100%", attrib={'stop-color': "#904e95"})
        linear_gradient.append(stop1)
        linear_gradient.append(stop2)

        rect = Et.Element('rect', xmlns="http://www.w3.org/2000/svg", x="0.5", y="0.5",
                          rx="4.5", height="99%", stroke="#e4e2e2", width="299", fill="url(#gradient)",
                          attrib={'stroke-opacity': '1'})

        self.root.append(rect)


class DarkTheme(BaseTheme):
    def __init__(self, *elements):
        super().__init__(*elements)
        self.root.append(css(
            header_fill='#58A6FF',
            lang_name_fill='#C3D1D9',
            stat_fill='#C3D1D9'
        ))

    def background(self):
        rect = Et.Element('rect',
                          xmlns="http://www.w3.org/2000/svg",
                          x="0.5", y="0.5", rx="4.5", height="99%",
                          stroke="#e4e2e2", width="299", fill="#0D1117",
                          attrib={'stroke-opacity': '1'})

        self.root.append(rect)


class MonokaiTheme(BaseTheme):
    def __init__(self, *elements):
        super().__init__(*elements)
        self.root.append(css(
            header_fill='#eb1f6a',
            lang_name_fill='#DEE2E4',
            stat_fill='#DEE2E4'
        ))

    def background(self):
        rect = Et.Element('rect',
                          xmlns="http://www.w3.org/2000/svg", x="0.5", y="0.5", rx="4.5",
                          height="99%", stroke="#e4e2e2", width="299",
                          fill="#272822",
                          attrib={'stroke-opacity': "1"})
        self.root.append(rect)


class AmbientGradientTheme(BaseTheme):
    def background(self):

        gradient = GradientGenerator(35,
                                     (0, '#4158d0'),
                                     (50, '#c850c0'),
                                     (100, '#ffcc70')).generate()
        self.root.append(gradient)
        rect = Et.Element('rect',
                          xmlns="http://www.w3.org/2000/svg", x="0.5", y="0.5", rx="4.5",
                          height="99%", stroke="#e4e2e2", width="299", fill="url(#gradient)",
                          attrib={'stroke-opacity': "1"})

        self.root.append(rect)


class OceanBlueGradient(BaseTheme):
    def background(self):
        gradient = GradientGenerator(35, (0, '#2E3192'), (100, '#1BFFFF')).generate()
        self.root.append(gradient)

        rect = Et.Element('rect', xmlns="http://www.w3.org/2000/svg", x="0.5", y="0.5",
                          rx="4.5", height="99%", stroke="#e4e2e2", width="299", fill="url(#gradient)",
                          attrib={'stroke-opacity': '1'})

        self.root.append(rect)


class EternalConstanceGradientTheme(BaseTheme):
    def background(self):
        gradient = GradientGenerator(0, (5, '#09203F'), (95, '#537895')).generate()
        self.root.append(gradient)

        rect = Et.Element('rect', xmlns="http://www.w3.org/2000/svg", x="0.5", y="0.5",
                          rx="4.5", height="99%", stroke="#e4e2e2", width="299", fill="url(#gradient)",
                          attrib={'stroke-opacity': '1'})

        self.root.append(rect)


class ViceCityGradientTheme(BaseTheme):
    def background(self):
        gradient = GradientGenerator(0, (5, '#3494e6'), (95, '#ec6ead')).generate()
        self.root.append(gradient)

        rect = Et.Element('rect', xmlns="http://www.w3.org/2000/svg", x="0.5", y="0.5",
                          rx="4.5", height="99%", stroke="#e4e2e2", width="299", fill="url(#gradient)",
                          attrib={'stroke-opacity': '1'})

        self.root.append(rect)


class PurpinkGradientTheme(BaseTheme):
    def background(self):
        gradient = GradientGenerator(0, (5, '#7f00ff'), (95, '#e100ff')).generate()
        self.root.append(gradient)

        rect = Et.Element('rect', xmlns="http://www.w3.org/2000/svg", x="0.5", y="0.5",
                          rx="4.5", height="99%", stroke="#e4e2e2", width="299", fill="url(#gradient)",
                          attrib={'stroke-opacity': '1'})

        self.root.append(rect)
