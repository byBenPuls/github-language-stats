from xml.etree import ElementTree as Et


class Element:
    def __init__(
        self,
        tag: str,
        attrib: dict[str, str] | None = None,
        *sub_elements,
        **extra: str,
    ) -> None:
        self.element = None
        if tag is None:
            raise ValueError("tag cannot be None")
        if attrib is None:
            attrib = {}
        self.tag = tag
        self.attrib = attrib
        self.sub_elements = sub_elements
        self.extra = extra
        self.text: str | None = None

    def render(self) -> Et.Element:
        self.element = Et.Element(self.tag, self.attrib, **self.extra)
        if self.text is not None:
            self.element.text = self.text
            
        for i in self.sub_elements:
            self.element.append(i.render())

        return self.element

    def __repr__(self):
        return "Element({}, {}, {}, {})".format(
            self.tag, self.attrib, self.sub_elements, self.extra
        )


class Group(Element):
    def __init__(
        self, attrib: dict[str, str] | None = None, *sub_elements, **extra: str
    ) -> None:
        if attrib is None:
            attrib = {}
        super().__init__("g", attrib=attrib, *sub_elements, **extra)
