from textnode import TextNode, text_type_text, text_type_link, text_type_italic, text_type_image, text_type_code, text_type_bold
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_node_delimiter import split_nodes_delimiter


def main():
    print("hello world from python!!")
    bold = TextNode("This is a *bold text node*", text_type_text)
    code = TextNode("This is a `code` text `node`", text_type_text)
    node = HTMLNode("a", "hola mundo", None, {"href":"github.com", "target":"_blank"})
    leaf = LeafNode("b", "This is a BOLD text.")
    leaf3 = LeafNode(None, "Normal text")
    leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    leaf3 = LeafNode(None, "Normal text 2")
    li = ParentNode("li", [leaf])
    li2 = ParentNode("li", [leaf2])
    li3 = ParentNode("li", [leaf3])
    ul = ParentNode("ul", [li, li2, li3], {"background-color":"red"})
    
    node = TextNode("This is text with a `code block` word", text_type_text)

    new_nodes = split_nodes_delimiter([node, code], "`", text_type_code)

    print(new_nodes)

main()