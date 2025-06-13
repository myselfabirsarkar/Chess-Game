# /* Kinght.py

import pygame
from data.classes.Piece import Piece


class Knight(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'F:/Chess/data/imgs/' + color[0] + '_knight.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'N'

    def get_possible_moves(self, board):
        output = []
        moves = [
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2)
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
    
"""
The provided code defines the Knight class which inherits from the Piece class and represents the knight piece in chess. Here's a breakdown of its functionalities:

1. Initialization:

__init__(self, pos, color, board):
Inherits attributes from the Piece class (pos, x, y, color, and has_moved).
Sets the knight's image path based on its color (e.g., "C:/Users/hillo/Documents/Python/Chess/data/imgs/w_knight.png" for white knight).
Loads the knight image using pygame.image.load.
Resizes the image to fit within the square dimensions on the board (accounting for a 20-pixel margin).
Sets the notation for the knight piece to 'N'.
2. Methods:

get_possible_moves(self, board) (Overrides parent class):
This method calculates all the possible squares the knight can move to, considering the unique L-shaped movement pattern of knights.
It creates a list of directions represented by offsets (one or two squares in either positive or negative x and y directions).
Iterates through each direction:
Calculates the new position based on the current position and the direction vector.
Checks if the new position is within the board boundaries (0 to 7 for both x and y coordinates).
If it's a valid position on the board, it appends the square object at that position (using board.get_square_from_pos) to the output list.
Knights can jump over other pieces, so there's no need to check if squares in between the starting and ending positions are empty.
Returns the list of squares representing the knight's possible moves.
In summary, the Knight class defines the specific movement logic for knights, which is an L-shaped pattern considering the board boundaries."""