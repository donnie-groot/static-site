###### standard library imports ######
#import os 

###### 3rd party imports ######
#import from thing i downloaded 

###### local imports ######
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        
        if old_node.text_type == TextType.TEXT:
            
            splited = old_node.text.split(delimiter)

            if len(splited) % 2 == 0:
                raise ValueError("invalid markdown, formatted")
            
            for i in range(len(splited)):

                if i % 2 == 0:
                    if splited[i]:
                        new_nodes.append(TextNode(splited[i], TextType.TEXT))

                else:
                    new_nodes.append(TextNode(splited[i], text_type))

        else:
            new_nodes.append(old_node)

    return new_nodes