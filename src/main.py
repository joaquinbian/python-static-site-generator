from textnode import TextNode
from htmlnode import HTMLNode, LeafNode


def main():
    print("hello world from python!!")
    bold = TextNode("This is a text node", "bold")
    bold2 = TextNode("This is a text node", "bold")
    node = HTMLNode("a", "hola mundo", None, {"href":"github.com", "target":"_blank"})
    leaf = LeafNode("p", "This is a paragraph of text.")
    leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    
    print(leaf.to_html())
    print(leaf2.to_html())

main()