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
        if not node in self._children:
            self._children.append(node)


    def remove_child(self, node):
        if node in self._children:
            self._children.pop(node)
            self._parent = None


    @property
    def parent(self):
        return self._parent


    @parent.setter
    def parent(self, node):
        self._parent = node
        node.add_child(self)
