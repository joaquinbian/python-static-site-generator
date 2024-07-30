from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.value = value
   
    

    def to_html(self):
        if self.value == None:
            raise ValueError("all leaf nodes must have a value")
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
    

            
