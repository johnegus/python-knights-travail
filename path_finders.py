from tree import Node

class KnightPathFinder:
    def __init__(self, positions):
        self._root = Node(positions)
        self._considered_positions = set(positions)

    def get_valid_moves(self, pos):
        validmoves = [(2, 1), (2, -1), (-2, 1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        
        moves = [] 
        
        for move in validmoves: 
            new_x = pos[0] + move[0]
            new_y = pos[1] + move[1]
            if new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8:
                moves.append((new_x, new_y))
        return moves 
    
    # def new_move_positions(self, pos):

start = KnightPathFinder((0, 0))
print(start.get_valid_moves(0,0))