###### standard library imports ######
from enum import Enum

###### 3rd party imports ######
#import from thing i downloaded 

###### local imports ######
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, text_node_to_html_node, TextType
 


def markdown_to_blocks(markdown): 
    blocks = []
    splitted = markdown.split("\n\n")

    for string in splitted:
        formatted = string.strip()

        if formatted == "":
            continue
        blocks.append(formatted)

    return blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown):
    if markdown.startswith("# ") or markdown.startswith("## ") or markdown.startswith("### ") or markdown.startswith("#### ") or markdown.startswith("##### ") or markdown.startswith("###### "):
        return BlockType.HEADING

    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE

# quotes

    lines = markdown.split("\n")
    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE

#unordered list 

    lines = markdown.split("\n")
    is_list = True
    for line in lines:
        if not line.startswith("- "):
            is_list = False
            break
    if is_list:
        return BlockType.UNORDERED_LIST

# ordered list

    lines = markdown.split("\n")
    is_ordered = True
    count = 1
    for line in lines:
        if not line.startswith(f"{count}. "):
            is_ordered = False
            break
        count += 1
    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)

    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    parpagraph_text = " ".join(lines)
    children = text_to_children(parpagraph_text)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break

    string = block[level + 1:]

    children = text_to_children(string)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    text = block[4:-4]
    text_node = TextNode(text, TextType.TEXT)
    html_node = text_node_to_html_node(text_node)

    child_node = ParentNode("code", [html_node])
    pre = ParentNode("pre", [child_node])

    return pre


def quote_to_html_node(block):
    split = block.split("\n")
    new_lines = []
    
    for line in split:
        words = line.lstrip("> ")
        new_lines.append(words)

    string = " ".join(new_lines)

    children = text_to_children(string)
    return ParentNode("blockquote", children)
    

def unordered_list_to_html_node(block):
    split = block.split("\n")
    html_items = []

    for word in split:
        text = word[2:]
        children = text_to_children(text)
        li = ParentNode("li", children)
        html_items.append(li)

    return ParentNode("ul", html_items)
        
        
def ordered_list_to_html_node(block):
    split = block.split("\n")
    html_items = []

    for line in split:
        text = line.split(". ", 1)[1]
        children = text_to_children(text)
        li = ParentNode("li", children)
        html_items.append(li)

    return ParentNode("ol", html_items)


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)

    return ParentNode("div", children)