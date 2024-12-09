# /* King.py

import pygame
from data.classes.Piece import Piece


class King(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'F:/Chess/data/imgs/' + color[0] + '_king.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'K'

    def get_possible_moves(self, board):
        output = []
        moves = [
            (0,-1), # north
            (1, -1), # ne
            (1, 0), # east
            (1, 1), # se
            (0, 1), # south
            (-1, 1), # sw
            (-1, 0), # west
            (-1, -1), # nw
        ]
        for move in moves:
            new_pos = (self.x + move[0], self.y + move[1])
            if (
                new_pos[0] < 8 and
                new_pos[0] >= 0 and 
                new_pos[1] < 8 and 
                new_pos[1] >= 0
            ):
                output.append([
                    board.get_square_from_pos(
                        new_pos
                    )
                ])
        return output

    def can_castle(self, board):
        if not self.has_moved:
            if self.color == 'white':
                queenside_rook = board.get_piece_from_pos((0, 7))
                kingside_rook = board.get_piece_from_pos((7, 7))
                if queenside_rook != None:
                    if not queenside_rook.has_moved:
                        if [
                            board.get_piece_from_pos((i, 7)) for i in range(1, 4)
                        ] == [None, None, None]:
                            return 'queenside'
                if kingside_rook != None:
                    if not kingside_rook.has_moved:
                        if [
                            board.get_piece_from_pos((i, 7)) for i in range(5, 7)
                        ] == [None, None]:
                            return 'kingside'
            elif self.color == 'black':
                queenside_rook = board.get_piece_from_pos((0, 0))
                kingside_rook = board.get_piece_from_pos((7, 0))
                if queenside_rook != None:
                    if not queenside_rook.has_moved:
                        if [
                            board.get_piece_from_pos((i, 0)) for i in range(1, 4)
                        ] == [None, None, None]:
                            return 'queenside'
                if kingside_rook != None:
                    if not kingside_rook.has_moved:
                        if [
                            board.get_piece_from_pos((i, 0)) for i in range(5, 7)
                        ] == [None, None]:
                            return 'kingside'

    def get_valid_moves(self, board):
        output = []
        for square in self.get_moves(board):
            if not board.is_in_check(self.color, board_change=[self.pos, square.pos]):
                output.append(square)
        if self.can_castle(board) == 'queenside':
            output.append(
                board.get_square_from_pos((self.x - 2, self.y))
            )
        if self.can_castle(board) == 'kingside':
            output.append(
                board.get_square_from_pos((self.x + 2, self.y))
            )
        return output
    
"""
This code defines the King class which inherits from the Piece class and represents the king piece in chess. Here's a breakdown of its functionalities:

1. Initialization:

__init__(self, pos, color, board):
Inherits attributes from the Piece class (pos, x, y, color, and has_moved).
Sets the king's image path based on its color (e.g., "C:/Users/hillo/Documents/Python/Chess/data/imgs/w_king.png" for white king).
Loads the king image using pygame.image.load.
Resizes the image to fit within the square dimensions on the board (accounting for a 20-pixel margin).
Sets the notation for the king piece to 'K'.
2. Methods:

get_possible_moves(self, board) (Overrides parent class):

This method calculates all the possible squares the king can move to without considering if those moves would put itself in check.
It creates a list of directions (one square move in each of the eight cardinal directions: north, northeast, east, southeast, south, southwest, west, northwest).
Iterates through each direction:
Calculates the new position based on the current position and the direction vector.
Checks if the new position is within the board boundaries (0 to 7 for both x and y coordinates).
If it's a valid position on the board, it appends the square object at that position (using board.get_square_from_pos) to the output list.
Returns the list of squares representing the king's possible moves without considering if they are safe.
can_castle(self, board):

This method checks if the king can castle (a special king move involving a rook jump) in either direction (queenside or kingside).
It first verifies if the king hasn't moved yet (not self.has_moved).
For white king:
Checks for the presence of rooks on the starting squares (queenside at (0, 7) and kingside at (7, 7)).
If the queenside rook exists and hasn't moved, it further checks if the squares between the king and the rook are empty.
Similar checks are performed for the kingside rook.
Similar logic is applied for black king, but considering the starting squares at (0, 0) and (7, 0) for the rooks.
If the conditions for castling are met (king and rook not moved, empty squares between them), the method returns either 'queenside' or 'kingside' depending on the applicable rook.
If castling is not possible, it returns None.
get_valid_moves(self, board):

This method considers both possible moves (from get_moves) and safety to determine the valid moves for the king.
It iterates through the possible moves obtained from get_moves:
For each square, it uses board.is_in_check to check if moving the king to that square would put it in check.
If the move doesn't lead to check, the square is appended to the output list of valid moves.
Additionally, it checks if castling is possible using can_castle.
If castling is possible (either queenside or kingside), the corresponding squares for castling are appended to the valid moves list (obtained using board.get_square_from_pos).
Finally, it returns the list of valid moves for the king, considering both safety and castling possibilities."""