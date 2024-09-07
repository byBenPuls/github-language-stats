from typing import Iterable

from src.svg.elements import Element


class CssBuilder:
    def __init__(self, code: dict[str, dict[str, str | dict[str, str]]]) -> None:
        self.code = code

    @staticmethod
    def insert_css_to_element(css_code: str) -> Element:
        style = Element(tag="style")
        style.text = css_code
        return style

    def serialize_property(self, name: str, data: str | dict) -> str:
        match data:
            case str():
                return f"\t{name}: {data};"
            case dict():
                return "\n\t\t".join(
                    f"\t{name} {{{self.serialize_property(key, value)}}}"
                    for key, value in data.items()
                )

    @staticmethod
    def serialize_selector(name: str, properties: Iterable[str]) -> str:
        match name:
            # case ["@keyframes" | "@media" | "@supports" as rule] if rule in name:
            #     return f"\t{name} {{\n\t\t{'\n'.join(properties)}\n\t}}"
            case _:
                return f"{name} {{\n{'\n'.join(properties)}\n}}"

    @staticmethod
    def combine_selectors(selectors: Iterable[str]) -> str:
        return "\n".join(selectors)

    def create_selector(
        self, selector_name: str, selector_properties: dict[str, str]
    ) -> str:
        properties = (
            self.serialize_property(k, v) for k, v in selector_properties.items()
        )
        construction = self.serialize_selector(selector_name, properties)
        return construction

    def build(self) -> Element:
        selectors = (i for i in self.code.items())
        serialized_data = (
            self.create_selector(s_name, s_properties)
            for s_name, s_properties in selectors
        )
        css_text = self.combine_selectors(serialized_data)

        return self.insert_css_to_element(css_text)

    def __str__(self) -> str:
        return self.build().text

    def __getitem__(self, item) -> dict[str, str]:
        return self.code[item]
