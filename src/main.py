from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode



def main():
    print("hello world from python!!")
    bold = TextNode("This is a text node", "bold")
    bold2 = TextNode("This is a text node", "bold")
    node = HTMLNode("a", "hola mundo", None, {"href":"github.com", "target":"_blank"})
    leaf = LeafNode("b", "This is a BOLD text.")
    leaf3 = LeafNode(None, "Normal text")
    leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    leaf3 = LeafNode(None, "Normal text 2")
    li = ParentNode("li", [leaf])
    li2 = ParentNode("li", [leaf2])
    li3 = ParentNode("li", [leaf3])
    ul = ParentNode("ul", [li, li2, li3], {"background-color":"red"})
    
    print(ul.to_html())

main()