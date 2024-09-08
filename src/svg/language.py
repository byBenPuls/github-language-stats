from src.svg.elements import Element, Group


class LanguageLabel:
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def create_label(self) -> Element:
        element = Element(tag="text", x="15", y="10", fill="black", id="lang-name")
        element.text = self.name
        return element

    def create_circle(self) -> Element:
        element = Element(tag="circle", cx="5", cy="6", fill=self.color, r="5")
        return element

    def build(self) -> Element:
        return Group(self.create_circle(), self.create_label())
