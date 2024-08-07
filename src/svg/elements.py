import logging
from xml.etree import ElementTree as Et

logger = logging.getLogger("uvicorn.info")


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
            raise ValueError("tag cannot be None")
        if attrib is None:
            attrib = {}
        self.tag = tag
        self.attrib = attrib
        self.sub_elements = sub_elements
        self.extra = extra
        self.text: str | None = None

    def render(self) -> Et.Element:
        logger.info(self)
        self.element = Et.Element(self.tag, self.attrib, **self.extra)
        for sub_element in self.sub_elements:
            if isinstance(sub_element, Element):
                sub_element = sub_element.render()
            else:
                sub_element = sub_element
            self.element.append(sub_element)
        if self.text:
            self.element.text = self.text
        return self.element

    def __repr__(self):
        return "Element({}, {}, {}, {})".format(
            self.tag, self.attrib, self.sub_elements, self.extra
        )


class Group(Element):
    def __init__(self, *sub_elements, **extra: str) -> None:
        super().__init__(tag="g", *sub_elements, **extra)
