# /* Rook.py

import pygame
from data.classes.Piece import Piece


class Rook(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'F:/Chess/data/imgs/' + color[0] + '_rook.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'R'

    def get_possible_moves(self, board):
        output = []
        moves_north = []
        for y in range(self.y)[::-1]:
            moves_north.append(board.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_north)
        moves_east = []
        for x in range(self.x + 1, 8):
            moves_east.append(board.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_east)
        moves_south = []
        for y in range(self.y + 1, 8):
            moves_south.append(board.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_south)
        moves_west = []
        for x in range(self.x)[::-1]:
            moves_west.append(board.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_west)
        return output
    
"""
The provided code defines the Rook class which inherits from the Piece class and represents the rook piece in chess. Here's a breakdown of its functionalities:

1. Initialization:

__init__(self, pos, color, board):
Inherits attributes from the Piece class (pos, x, y, color, and has_moved).
Sets the rook's image path based on its color (e.g., "C:/Users/hillo/Documents/Python/Chess/data/imgs/w_rook.png" for white rook).
Loads the rook image using pygame.image.load.
Resizes the image to fit within the square dimensions on the board (accounting for a 20-pixel margin).
Sets the notation for the rook piece to 'R'.
2. Methods:

get_possible_moves(self, board) (Overrides parent class):
This method calculates all the possible squares the rook can move to. Rooks can move any number of squares horizontally (left or right) and vertically (up or down) as long as the path is not blocked by other pieces.
It utilizes four loops, one for each direction (north, east, south, and west).
For each direction:
It creates a list to store the squares in that direction.
It iterates through squares in the chosen direction until it goes off the board (index out of range).
Within the loop, it gets the square object at the current position using board.get_square_from_pos.
It appends the square object to the direction-specific list.
Finally, it returns a list of lists, where each sub-list represents the possible moves in a particular direction.
In summary, the Rook class defines the movement logic for rooks, allowing them to move horizontally and vertically across any number of squares on an unobstructed path."""