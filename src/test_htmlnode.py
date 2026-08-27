import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_none(self):
        node = HTMLNode()
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_eq_empty_dict(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_eq_two_props(self):
        node = HTMLNode(props={"href": "https://www.boot.dev", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.boot.dev" target="_blank"')