###### standard library imports ######
#import os 

###### 3rd party imports ######
#import from thing i downloaded 

###### local imports ######
from copystatic import copy_file_recursive, delete_and_recreate
from gencontent import  generate_pages_recursive


def main():  
    delete_and_recreate("public")
    copy_file_recursive("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()