# /* Queen.py

import pygame
from data.classes.Piece import Piece


class Queen(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'F:/Chess/data/imgs/' + color[0] + '_queen.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'Q'

    def get_possible_moves(self, board):
        output = []
        moves_north = []
        for y in range(self.y)[::-1]:
            moves_north.append(board.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_north)
        moves_ne = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y - i < 0:
                break
            moves_ne.append(board.get_square_from_pos(
                (self.x + i, self.y - i)
            ))
        output.append(moves_ne)
        moves_east = []
        for x in range(self.x + 1, 8):
            moves_east.append(board.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_east)
        moves_se = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y + i > 7:
                break
            moves_se.append(board.get_square_from_pos(
                (self.x + i, self.y + i)
            ))
        output.append(moves_se)
        moves_south = []
        for y in range(self.y + 1, 8):
            moves_south.append(board.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_south)
        moves_sw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y + i > 7:
                break
            moves_sw.append(board.get_square_from_pos(
                (self.x - i, self.y + i)
            ))
        output.append(moves_sw)
        moves_west = []
        for x in range(self.x)[::-1]:
            moves_west.append(board.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_west)
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
The provided code defines the Queen class which inherits from the Piece class and represents the queen piece in chess. Here's a breakdown of its functionalities:

1. Initialization:

__init__(self, pos, color, board):
Inherits attributes from the Piece class (pos, x, y, color, and has_moved).
Sets the queen's image path based on its color (e.g., "C:/Users/hillo/Documents/Python/Chess/data/imgs/w_queen.png" for white queen).
Loads the queen image using pygame.image.load.
Resizes the image to fit within the square dimensions on the board (accounting for a 20-pixel margin).
Sets the notation for the queen piece to 'Q'.
2. Methods:

get_possible_moves(self, board) (Overrides parent class):
This method calculates all the possible squares the queen can move to, combining the movement patterns of rooks (horizontal and vertical movements) and bishops (diagonal movements).
It utilizes eight loops, one for each direction (north, northeast, east, southeast, south, southwest, west, northwest).
For each direction:
It creates a list to store the squares in that direction.
It iterates through squares in the chosen direction until it goes off the board (index out of range).
Within the loop, it gets the square object at the current position using board.get_square_from_pos.
It appends the square object to the direction-specific list.
Finally, it returns a list of lists, where each sub-list represents the possible moves in a particular direction.
In summary, the Queen class combines the functionalities of rooks and bishops, allowing it to move any number of squares in horizontal, vertical, and diagonal directions as long as the path is not blocked by other pieces (except for the square it lands on)."""