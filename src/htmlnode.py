class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("dev still working on method sorry")


    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html


    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__( tag, value, None, props)


    def to_html(self):
        if self.value is None:
            raise ValueError("value is none")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children ,props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is none please add a tag")
        if self.children is None:
            raise ValueError("your child is missing please add a child")

        child_html = ""
        for child in self.children:
            child_html += child.to_html()
            
        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"