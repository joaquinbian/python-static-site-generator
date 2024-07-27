import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_diff(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
        

    def test_no_url(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        test_repr = "TextNode(This is a text node, bold, None)"

        self.assertEqual(node.__repr__(), test_repr)
    


if __name__ == "__main__":
    unittest.main()