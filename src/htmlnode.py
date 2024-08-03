class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        str = ""
        if self.props != None:
            for key, value in self.props.items():
                str += f" {key}='{value}'"
        return str
    
    def __repr__(self):
        return f"HTMLNode('{self.tag}', '{self.value}', children={self.children}, props={self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        elif not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, children={self.children}, props={self.props})"
    


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent Nodes should have a tag")
        elif not self.children:
            raise ValueError("Parent Nodes must have children")
        elif not isinstance(self.children, list):
            raise ValueError("children prop must be a list")
        else:
            str = ""
            strList = list(map(lambda x: x.to_html(), self.children))
            for elem in strList:
                str += elem 
            return f"<{self.tag}{self.props_to_html()}>{str}</{self.tag}>"