from tree import Node


class KnightPathFinder:
    def __init__(self, positions):
        self._root = Node(positions)
        self._considered_positions = set(positions)

    def get_valid_moves(self, pos):
        validmoves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                      (1, 2), (1, -2), (-1, 2), (-1, -2)]

        moves = []

        for move in validmoves:
            new_x = pos[0] + move[0]
            new_y = pos[1] + move[1]
            if new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8:
                moves.append((new_x, new_y))
        return moves

    def new_move_positions(self, pos):
        moves = set(self.get_valid_moves(pos))
        newmoves = moves.difference(self._considered_positions)
        self._considered_positions = self._considered_positions.union(newmoves)
        return newmoves

    def build_move_tree(self):
        moves_tree = []
        queue = [self._root]
        
        while queue:
            node = queue.pop(0)
            moves = self.new_move_positions(node.value)
            node._considered_positions = moves
            for move in moves:
                new = Node(move)
                node.add_child(new)
                moves_tree.append(new)
        return moves_tree

# finder = KnightPathFinder((0, 0))
# print(finder.get_valid_moves((5, 5)))
# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))
finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder._root.children)

# def breadth_search(self, value):
#     search = [self]

#     while search:
#         node = search.pop(0)
#         if node._value == value:
#             return node
#         search.extend(node._children)

#     return None
