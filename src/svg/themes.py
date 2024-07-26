from xml.etree import ElementTree as Et

themes = (
    'main',
    'gradient',
    'dark',
    'monokai',
    'ambient_gradient'
)


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
        self.root.append(css())

    def background(self):
        raise NotImplementedError

    def insert(self):
        for i in self.elements:
            self.root.append(i)

    def card(self):
        self.background()
        self.insert()
        return self.root


class MainTheme(BaseTheme):
    def background(self):
        rect = Et.Element('rect', x='0.5', y='0.5',
                          rx="4.5", height="99%", stroke="#e4e2e2",
                          width="299", fill="#fffefe")

        self.root.append(rect)


class GradientTheme(BaseTheme):
    def __init__(self, *elements):
        super().__init__(*elements)
        self.root.append(css(
            header_fill='#fff',
            lang_name_fill='#fff',
            stat_fill='#fff'
        ))

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
                          rx="4.5", height="99%", stroke="#e4e2e2", width="449", fill="url(#gradient)",
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
                          stroke="#e4e2e2", width="466", fill="#0D1117",
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
                          height="99%", stroke="#e4e2e2", width="399",
                          fill="#272822",
                          attrib={'stroke-opacity': "1"})
        self.root.append(rect)


class AmbientGradientTheme(BaseTheme):
    def __init__(self, *elements):
        super().__init__(*elements)
        self.root.append(css(
            header_fill='#fff',
            lang_name_fill='#fff',
            stat_fill='#fff'
        ))

    def background(self):

        defs = Et.Element('defs', xmlns="http://www.w3.org/2000/svg")
        self.root.append(defs)
        linear_gradient = Et.Element('linearGradient', id="gradient", gradientTransform="rotate(35)",
                                     gradientUnits="userSpaceOnUse")
        defs.append(linear_gradient)
        stop1 = Et.Element('stop', offset="0%", attrib={'stop-color': "#4158d0"})
        stop2 = Et.Element('stop', offset="50%", attrib={'stop-color': "#c850c0"})
        stop3 = Et.Element('stop', offset="100%", attrib={'stop-color': "#ffcc70"})
        linear_gradient.append(stop1)
        linear_gradient.append(stop2)
        linear_gradient.append(stop3)

        rect = Et.Element('rect',
                          xmlns="http://www.w3.org/2000/svg", x="0.5", y="0.5", rx="4.5",
                          height="99%", stroke="#e4e2e2", width="466", fill="url(#gradient)",
                          attrib={'stroke-opacity': "1"})

        self.root.append(rect)
