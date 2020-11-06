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

    def find_path(self, end_position):
        node = self._root.breadth_search(end_position)
        path = [node.value for node in self.trace_to_root(node)]
        return sorted(path)

    def trace_to_root(self, end_node):
        route = []
        current = end_node
        while current:
            route.append(current)
            if current.parent is not None:
                current = current.parent
            else:
                current = None

        return route




# finder = KnightPathFinder((0, 0))
# print(finder.get_valid_moves((5, 5)))
# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))
# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder._root.children)

finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder.find_path((2, 1)))  # => [(0, 0), (2, 1)]
print(finder.find_path((3, 3)))  # => [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
# => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
print(finder.find_path((7, 6)))
