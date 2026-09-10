###### standard library imports ######
#import os 

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