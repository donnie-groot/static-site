from textnode import TextNode, TextType


def main():
    my_node = TextNode("test text", TextType.PLAIN_TEXT, "google.com")
    print(my_node)

main()

