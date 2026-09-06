###### standard library imports ######
import re

###### 3rd party imports ######
#import from thing i downloaded 

###### local imports ######
from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter




def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        original_text = node.text 

        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))


            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

    
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        original_text = node.text 

        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(link[0], TextType.LINKS, link[1]))


            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
    