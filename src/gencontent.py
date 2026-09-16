###### standard library imports ######
import os
from pathlib import Path

###### 3rd party imports ######
#import from thing i downloaded 

###### local imports ######
from markdown_to_blocks import  markdown_to_html_node




def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            result = line[2:].strip()
            return result
        
    raise Exception("no title found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} useing {template_path}")

    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template_content = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)

    des_dir = os.path.dirname(dest_path)
    os.makedirs(des_dir, exist_ok=True)

    dest_file = open(dest_path, "w")
    dest_file.write(template_content)
    dest_file.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for path in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, path)
        dest_path = os.path.join(dest_dir_path, path)

        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)

        else:
            generate_pages_recursive(from_path, template_path, dest_path)