from textnode import TextNode
from htmlnode import HTMLNode

def main():
    print("hello world from python!!")
    bold = TextNode("This is a text node", "bold")
    bold2 = TextNode("This is a text node", "bold")
    node = HTMLNode("a", "hola mundo", None, {"href":"github.com", "target":"_blank"})
    print(node.__repr__())
    print(bold)

main()