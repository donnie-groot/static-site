import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("this is a test", TextType.TEXT)
        node2 = TextNode("this is a test", TextType.ITALIC)
        self.assertNotEqual(node,node2)

    def test_not_eq_dif_txt(self):
        node = TextNode("this is a test", TextType.BOLD)
        node2 = TextNode(" this is a diffrent test", TextType.BOLD )
        self.assertNotEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("this is a test", TextType.BOLD, None)
        node2 = TextNode("this is a test", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    

if __name__ == "__main__":
    unittest.main()
