###### standard library imports ######
import sys

###### 3rd party imports ######
#import from thing i downloaded 

###### local imports ######
from copystatic import copy_file_recursive, delete_and_recreate
from gencontent import  generate_pages_recursive


def main():  
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
        
    delete_and_recreate("docs")
    copy_file_recursive("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", base_path)
if __name__ == "__main__":
    main()