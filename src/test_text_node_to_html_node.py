import unittest

from htmlnode import LeafNode
from textnode import TextNode, text_type_text, text_type_bold, text_type_code, text_type_image, text_node_to_html_node

class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        p = TextNode("soy un texto", text_type_text)
        leaf_p = text_node_to_html_node(p)
        self.assertEqual(leaf_p.to_html(), "soy un texto")
    
    def test_bold_text(self):
        b = TextNode("soy un bold", text_type_bold)
        leaf_b = text_node_to_html_node(b)
        self.assertEqual(leaf_b.to_html(), "<b>soy un bold</b>")
    
    def test_code_text(self):
        c = TextNode("soy un code", text_type_code)
        leaf_c = text_node_to_html_node(c)
        self.assertEqual(leaf_c.to_html(), "<code>soy un code</code>")
    
    def test_image(self):
        img = TextNode("github image", text_type_image, "github.com")
        leaf_img = text_node_to_html_node(img)
        self.assertEqual(leaf_img.to_html(), "<img src='github.com' alt='github image'></img>")
    

    


            
    


if __name__ == "__main__":
    unittest.main()