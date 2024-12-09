# /* Bishop.py

import pygame
from data.classes.Piece import Piece


class Bishop(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'F:/Chess/data/imgs/' + color[0] + '_bishop.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'B'

    def get_possible_moves(self, board):
        output = []
        moves_ne = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y - i < 0:
                break
            moves_ne.append(board.get_square_from_pos(
                (self.x + i, self.y - i)
            ))
        output.append(moves_ne)
        moves_se = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y + i > 7:
                break
            moves_se.append(board.get_square_from_pos(
                (self.x + i, self.y + i)
            ))
        output.append(moves_se)
        moves_sw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y + i > 7:
                break
            moves_sw.append(board.get_square_from_pos(
                (self.x - i, self.y + i)
            ))
        output.append(moves_sw)
        moves_nw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y - i < 0:
                break
            moves_nw.append(board.get_square_from_pos(
                (self.x - i, self.y - i)
            ))
        output.append(moves_nw)
        return output

"""
This code defines the Bishop class which inherits from the Piece class and represents the bishop piece in chess. Here's a breakdown of its functionalities:

1. Initialization:

__init__(self, pos, color, board):
Inherits attributes from the Piece class (pos, x, y, color, and has_moved).
Sets the bishop's image path based on its color (e.g., "C:/Users/hillo/Documents/Python/Chess/data/imgs/w_bishop.png" for white bishop).
Loads the bishop image using pygame.image.load.
Resizes the image to fit within the square dimensions on the board (accounting for a 20-pixel margin).
Sets the notation for the bishop piece to 'B'.
2. Methods:

get_possible_moves(self, board) (Overrides parent class):
This method defines how bishops move on the chessboard.
It calculates possible moves in all four diagonal directions (northeast, southeast, southwest, northwest).
For each direction, it iterates through squares in a loop:
If the square goes off the board (index out of range), the loop for that direction is terminated.
Otherwise, it gets the square object at the current position in the loop using board.get_square_from_pos.
It appends the square to a list representing the possible moves in that direction.
Finally, it returns a list of lists, where each sub-list represents the possible moves in a particular diagonal direction."""