import unittest

from htmlnode import LeafNode, HTMLNode


class TestLeafNode(unittest.TestCase):
    def test_props(self):
        props = {"href":"github.com", "target":"_blank"}
        node = LeafNode("a", "hola mundo", props)
        propsStr = " href='github.com' target='_blank'"
        
        self.assertEqual(node.props_to_html(), propsStr)
    
    def test_leaf(self):
        node = LeafNode("p", "Hola mundo")
        str = "<p>Hola mundo</p>"
        self.assertEqual(node.to_html(), str)
    
    def test_is_an_HTMLNode(self):
        node = LeafNode("p", "Hola mundo")
        self.assertTrue(isinstance(node, HTMLNode))
    
    def test_repr(self):
        node = LeafNode("p", "Hola mundo")
        str = "LeafNode(p, Hola mundo, children=None, props=None)"
        self.assertEqual(node.__repr__(), str)
    
   

if __name__ == "__main__":
    unittest.main()