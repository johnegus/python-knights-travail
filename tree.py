class Node:
    def __init__(self, value):
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
        if node not in self._children:
            self._children.append(node)
            node._parent = self
        if self._parent is None:
            self._parent = node

    def remove_child(self, node):
        if node in self._children:
            self._children.pop(node)
            # self._parent = None
            node._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        # if self._parent:
        # node = self._parent
        # node.remove_child(self)
        self._parent = node
        # node.add_child(self)
        self._parent.add_child(self)
