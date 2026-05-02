import os

from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, filename)
        dst_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(src_path):
            dst_html = Path(dst_path).with_suffix(".html")
            generate_page(src_path, template_path, dst_html, basepath)
        else:
            generate_pages_recursive(src_path, template_path, dst_path, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as f:
        path_contents = f.read()

    html_content = markdown_to_html_node(path_contents).to_html()
    title = extract_title(path_contents)

    with open(template_path, "r") as f:
        template_contents = f.read()
        
    page = template_contents.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html_content)
    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(page)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No h1 header found")

