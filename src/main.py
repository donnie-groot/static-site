###### standard library imports ######
#import os 

###### 3rd party imports ######
#import from thing i downloaded 

###### local imports ######
from textnode import TextNode
from copystatic import copy_file_recursive, delete_and_recreate
from gencontent import generate_page


def main():  
    delete_and_recreate("public")
    copy_file_recursive("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()