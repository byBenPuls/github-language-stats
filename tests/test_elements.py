from xml.etree.ElementTree import tostring, ElementTree

from src.svg.elements import Element, Group


import pytest


def test_element_generation():
    element = Element(tag="svg")
    element.text = "Hello World!"

    element_in_bytes = tostring(element.render())

    assert element.tag == "svg"
    assert element_in_bytes == b"<svg>Hello World!</svg>"


def test_nested_tags():
    nested_elements = Element(Element(tag="style"), tag="svg")

    main_element_in_bytes = tostring(Group(nested_elements).render())
    assert main_element_in_bytes == b"<g><svg><style /></svg></g>"
