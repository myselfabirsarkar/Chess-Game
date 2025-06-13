# /* Pawn.py

import pygame
from data.classes.Piece import Piece


class Pawn(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'F:/Chess/data/imgs/' + color[0] + '_pawn.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 35, board.tile_height - 35))
        self.notation = ' '

    def get_possible_moves(self, board):
        output = []
        moves = []
        # move forward
        if self.color == 'white':
            moves.append((0, -1))
            if not self.has_moved:
                moves.append((0, -2))
        elif self.color == 'black':
            moves.append((0, 1))
            if not self.has_moved:
                moves.append((0, 2))
        for move in moves:
            new_pos = (self.x, self.y + move[1])
            if new_pos[1] < 8 and new_pos[1] >= 0:
                output.append(
                    board.get_square_from_pos(new_pos)
                )
        return output

    def get_moves(self, board):
        output = []
        for square in self.get_possible_moves(board):
            if square.occupying_piece != None:
                break
            else:
                output.append(square)
        if self.color == 'white':
            if self.x + 1 < 8 and self.y - 1 >= 0:
                square = board.get_square_from_pos(
                    (self.x + 1, self.y - 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        output.append(square)
            if self.x - 1 >= 0 and self.y - 1 >= 0:
                square = board.get_square_from_pos(
                    (self.x - 1, self.y - 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        output.append(square)
        elif self.color == 'black':
            if self.x + 1 < 8 and self.y + 1 < 8:
                square = board.get_square_from_pos(
                    (self.x + 1, self.y + 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        output.append(square)
            if self.x - 1 >= 0 and self.y + 1 < 8:
                square = board.get_square_from_pos(
                    (self.x - 1, self.y + 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        output.append(square)
        return output

    def attacking_squares(self, board):
        moves = self.get_moves(board)
        # return the diagonal moves 
        return [i for i in moves if i.x != self.x]
    
"""
The provided code defines the Pawn class which inherits from the Piece class and represents the pawn piece in chess. Here's a breakdown of its functionalities:

1. Initialization:

__init__(self, pos, color, board):
Inherits attributes from the Piece class (pos, x, y, color, and has_moved).
Sets the pawn's image path based on its color (e.g., "C:/Users/hillo/Documents/Python/Chess/data/imgs/w_pawn.png" for white pawn).
Loads the pawn image using pygame.image.load.
Resizes the image to fit within the square dimensions on the board (accounting for a 35-pixel margin on each side).
Sets the notation for the pawn piece to ' ' (empty space).
2. Methods:

get_possible_moves(self, board):

This method calculates all the possible squares a pawn could move to without considering if those moves would result in capturing other pieces.
It creates a list of moves based on the pawn's color:
White pawns can move forward one square (0, -1) and two squares for the first move (0, -2) if it hasn't moved yet.
Black pawns can move forward one square (0, 1) and two squares for the first move (0, 2) if it hasn't moved yet.
Iterates through each move in the list:
Calculates the new position based on the current position and the move vector.
Checks if the new position is within the board boundaries (0 to 7 for y-coordinate).
If it's a valid position on the board, it appends the square object at that position (using board.get_square_from_pos) to the output list.
This method considers all possible moves a pawn could take in a single turn, including capturing diagonally and moving forward one or two squares from the starting position. However, it doesn't consider if the squares are occupied by the pawn's own pieces.
get_moves(self, board):

This method refines the possible moves considering if the squares are empty or occupied by opponent pieces.
It calls get_possible_moves to get all possible squares the pawn could move to.
Iterates through the squares in the possible moves:
If a square is occupied by another piece, the loop breaks (pawns cannot jump over other pieces).
If the square is empty, it's appended to the output list.
Additionally, it checks for capturing moves diagonally (one square forward and one square left/right) depending on the pawn's color.
If there's an enemy piece on the diagonal square, it's appended to the output list.
This method essentially filters the possible moves from get_possible_moves to only include valid moves based on the board state (empty squares or capturing enemy pieces).
attacking_squares(self, board):

This method returns the squares that the pawn can attack, which are the diagonal squares forward-left and forward-right relative to the pawn's position.
It calls get_moves to get all possible moves (including capturing moves).
Filters the moves to only include squares where the x-coordinate is different from the pawn's x-coordinate (diagonal squares).
This method is useful for checking if a pawn can attack a specific square or if it's putting the opponent's king in check.
In summary, the Pawn class defines the logic for pawn movements considering its unique ability to move forward (one or two squares initially), capture diagonally, and the restriction of not jumping over other pieces."""