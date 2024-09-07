from xml.etree import ElementTree as Et

from src.exceptions import NotElementClassError, EmptyElementTagError


class Element:
    def __init__(
        self,
        *sub_elements,
        tag: str,
        attrib: dict[str, str] | None = None,
        **extra: str,
    ) -> None:
        self.element = None
        if tag is None:
            raise EmptyElementTagError
        if attrib is None:
            attrib = {}
        self.tag = tag
        self.attrib = attrib
        self.sub_elements = sub_elements
        self.extra = extra
        self.text: str | None = None

    def render(self) -> Et.Element:
        self.element = Et.Element(self.tag, self.attrib, **self.extra)
        for sub_element in self.sub_elements:
            match sub_element:
                case Element():
                    sub_element = sub_element.render()
                case Et.Element():
                    sub_element = sub_element
                case _:
                    raise NotElementClassError
            self.element.append(sub_element)
        if self.text:
            self.element.text = self.text
        return self.element

    def __repr__(self):
        return "Element({}, {}, {}, {}, '{}')".format(
            self.tag, self.attrib, self.sub_elements, self.extra, self.text
        )


class Group(Element):
    def __init__(self, *sub_elements, **extra: str) -> None:
        super().__init__(tag="g", *sub_elements, **extra)
