###### standard library imports ######
from enum import Enum

###### 3rd party imports ######
#import from thing i downloaded 

###### local imports ######





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



