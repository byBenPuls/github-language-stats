from src.svg.elements import Element


def create_custom_data_text(msg: str) -> Element:
    message = Element(
        tag="text",
        attrib={"text-anchor": "middle", "dominant-baseline": "middle"},
        x="50%",
        y="50%",
        fill="#434d58",
        id="stat",
    )
    message.text = msg
    return message
