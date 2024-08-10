import re

# images
#r"!\[(.*?)\]\((.*?)\)"

# regular links
#r"(?<!!)\[(.*?)\]\((.*?)\)"

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches
    