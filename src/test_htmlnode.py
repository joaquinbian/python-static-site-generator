import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        props = {"href":"github.com", "target":"_blank"}
        node = HTMLNode("a", "hola mundo", None, props)
        propsStr = " href='github.com' target='_blank'"
        
        self.assertEqual(node.props_to_html(), propsStr)
    
    def test_repr(self):
        props = {"href":"github.com", "target":"_blank"}
        node = HTMLNode("a", "hola mundo", None, props)
        anchorRepr = f"HTMLNode('a', 'hola mundo', children=None, props={props})"
        self.assertEqual(node.__repr__(), anchorRepr)

if __name__ == "__main__":
    unittest.main()