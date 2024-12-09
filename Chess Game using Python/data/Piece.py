# /* Piece.py

import pygame

class Piece:
    def __init__(self, pos, color, board):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.has_moved = False

    def get_moves(self, board):
        output = []
        for direction in self.get_possible_moves(board):
            for square in direction:
                if square.occupying_piece is not None:
                    if square.occupying_piece.color == self.color:
                        break
                    else:
                        output.append(square)
                        break
                else:
                    output.append(square)
        return output
    
    def get_valid_moves(self, board):
        output = []
        for square in self.get_moves(board):
            if not board.is_in_check(self.color, board_change=[self.pos, square.pos]):
                output.append(square)
        return output
    
    def move(self, board, square, force=False):
        for i in board.squares:
            i.highlight = False
        if square in self.get_valid_moves(board) or force:
            prev_square = board.get_square_from_pos(self.pos)
            self.pos, self.x, self.y = square.pos, square.x, square.y
            prev_square.occupying_piece = None
            square.occupying_piece = self
            board.selected_piece = None
            self.has_moved = True
            # Pawn promotion
            if self.notation == ' ':
                if self.y == 0 or self.y == 7:
                    from data.classes.pieces.Queen import Queen
                    square.occupying_piece = Queen(
                        (self.x, self.y),
                        self.color,
                        board
                    )
            # Move rook if king castles
            if self.notation == 'K':
                if prev_square.x - self.x == 2:
                    rook = board.get_piece_from_pos((0, self.y))
                    rook.move(board, board.get_square_from_pos((3, self.y)), force=True)
                elif prev_square.x - self.x == -2:
                    rook = board.get_piece_from_pos((7, self.y))
                    rook.move(board, board.get_square_from_pos((5, self.y)), force=True)
            return True
        else:
            board.selected_piece = None
            return False

    # True for all pieces except pawn
    def attacking_squares(self, board):
        return self.get_moves(board)

"""
This code defines the base class Piece for all chess pieces in the game. Here's a breakdown of its functionalities:

1. Attributes:

pos: Stores the piece's position as a tuple (x, y).
x and y: Separate attributes for x and y coordinates of the position.
color: Represents the color of the piece (e.g., "white" or "black").
has_moved: Boolean flag indicating if the piece has moved from its initial position.
2. Methods:

get_possible_moves(self, board): (Called by other methods)

This method likely defines the core logic for generating all possible squares the piece could move to without considering any obstacles or capturing other pieces. It's implemented by subclasses (like Rook) and not shown here.
get_moves(self, board):

Calls the get_possible_moves method to get all possible squares.
Iterates through the possible squares in each direction:
If a square is occupied by a piece of the same color, stops iterating in that direction as pieces cannot jump over their own pieces.
Otherwise, adds the square to the output list as a valid move (for now).
Returns the list of squares representing the piece's possible moves considering only its movement pattern and ignoring occupied squares.
get_valid_moves(self, board):

Calls the get_moves method to get all possible moves without considering check.
Iterates through the possible moves:
Uses the board.is_in_check method with a temporary board change (moving the piece to the current square) to check if the move would put the player's king in check.
If the move doesn't lead to check, adds the square to the output list as a valid move.
Returns the list of squares representing the piece's valid moves considering both its movement pattern and the check rule.
move(self, board, square, force=False):

Hides the highlight on all squares.
Checks if the target square is a valid move (using get_valid_moves) or if the force flag is set (used for special cases like castling).
If the move is valid:
Updates the piece's position attributes.
Updates the occupying piece references on the board squares (from and to).
Deselects the piece.
Sets the has_moved flag to True.
Handles pawn promotion: If the piece is a pawn reaching the other side of the board, it's replaced by a queen.
Handles kingside/queenside castling: If the piece is a king and has not moved before, it moves two squares in one direction, and the corresponding rook is moved to the adjacent square next to the king.
Returns True if the move was successful, False otherwise.
attacking_squares(self, board): (This method is likely overridden by subclasses)"""