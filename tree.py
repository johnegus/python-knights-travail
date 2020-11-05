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
    
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent is node:
            return
        if self._parent is not None:
            self._parent.remove_child(self)
        # if self._parent:
        #     node = self._parent
        #     node.remove_child(self)
        self._parent = node
        # node.add_child(self)
        if node is not None:
            node.add_child(self)

    def add_child(self, node):
        if node in self._children:
            return
        if node not in self._children:
            self._children.append(node)
            node.parent = self
        if self._parent is None:
            self.parent = node

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            # self._parent = None
            node.parent = None

    

node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)