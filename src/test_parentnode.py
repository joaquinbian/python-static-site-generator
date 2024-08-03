import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_parent_render(self):
        anchor = LeafNode("a", "Click me", {"href":"github.com"})
        normal = LeafNode(None, "Normal text")
        paragraph = ParentNode("p", [anchor, normal])
        str = "<p><a href='github.com'>Click me</a>Normal text</p>"

        self.assertEqual(paragraph.to_html(), str)
        self.assertTrue(anchor.props_to_html() in paragraph.to_html())
    
    def test_multiple_parents(self):
        anchor = LeafNode("a", "Github", {"href":"github.com"})
        anchor2 = LeafNode("a", "Google", {"href":"google.com"})
        li = ParentNode("li", [anchor])
        li2 = ParentNode("li", [anchor2])
        ul = ParentNode("ul", [li, li2])

        str = "<ul><li><a href='github.com'>Github</a></li><li><a href='google.com'>Google</a></li></ul>"
        self.assertEqual(ul.to_html(), str)
    


            
    


if __name__ == "__main__":
    unittest.main()