class Node:
    def __init__(self, value, parent, children):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value
    
    @property
    def children(self):
        return self._children
    
    def add_child(self, node):
        if not self._children[node]: 
            self._children.append(node)
