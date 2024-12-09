# /* Board.py

import pygame
from data.classes.Square import Square
from data.classes.pieces.Rook import Rook
from data.classes.pieces.Bishop import Bishop
from data.classes.pieces.Knight import Knight
from data.classes.pieces.Queen import Queen
from data.classes.pieces.King import King
from data.classes.pieces.Pawn import Pawn

# Game state checker
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_width = width // 8
        self.tile_height = height // 8
        self.selected_piece = None
        self.turn = 'white'
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.squares = self.generate_squares()
        self.setup_board()

    def generate_squares(self):
        output = []
        for y in range(8):
            for x in range(8):
                output.append(
                    Square(x,  y, self.tile_width, self.tile_height)
                )
        return output

    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square

    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).occupying_piece
    
    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square_from_pos((x, y))
                    # looking inside contents, what piece does it have
                    if piece[1] == 'R':
                        square.occupying_piece = Rook(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    # as you notice above, we put `self` as argument, or means our class Board
                    elif piece[1] == 'N':
                        square.occupying_piece = Knight(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'B':
                        square.occupying_piece = Bishop(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'Q':
                        square.occupying_piece = Queen(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'K':
                        square.occupying_piece = King(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'P':
                        square.occupying_piece = Pawn(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    if piece[1] == 'R':
                        square.occupying_piece = Rook(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
    
    def handle_click(self, mx, my):
        x = mx // self.tile_width
        y = my // self.tile_height
        clicked_square = self.get_square_from_pos((x, y))
        if self.selected_piece is None:
            if clicked_square.occupying_piece is not None:
                if clicked_square.occupying_piece.color == self.turn:
                    self.selected_piece = clicked_square.occupying_piece
        elif self.selected_piece.move(self, clicked_square):
            self.turn = 'white' if self.turn == 'black' else 'black'
        elif clicked_square.occupying_piece is not None:
            if clicked_square.occupying_piece.color == self.turn:
                self.selected_piece = clicked_square.occupying_piece
    
    # check state checker
    def is_in_check(self, color, board_change=None): # board_change = [(x1, y1), (x2, y2)]
        output = False
        king_pos = None
        changing_piece = None
        old_square = None
        new_square = None
        new_square_old_piece = None
        if board_change is not None:
            for square in self.squares:
                if square.pos == board_change[0]:
                    changing_piece = square.occupying_piece
                    old_square = square
                    old_square.occupying_piece = None
            for square in self.squares:
                if square.pos == board_change[1]:
                    new_square = square
                    new_square_old_piece = new_square.occupying_piece
                    new_square.occupying_piece = changing_piece
        pieces = [
            i.occupying_piece for i in self.squares if i.occupying_piece is not None
        ]
        if changing_piece is not None:
            if changing_piece.notation == 'K':
                king_pos = new_square.pos
        if king_pos == None:
            for piece in pieces:
                if piece.notation == 'K' and piece.color == color:
                        king_pos = piece.pos
        for piece in pieces:
            if piece.color != color:
                for square in piece.attacking_squares(self):
                    if square.pos == king_pos:
                        output = True
        if board_change is not None:
            old_square.occupying_piece = changing_piece
            new_square.occupying_piece = new_square_old_piece
        return output
    
    # checkmate state checker
    def is_in_checkmate(self, color):
        output = False
        for piece in [i.occupying_piece for i in self.squares]:
            if piece != None:
                if piece.notation == 'K' and piece.color == color:
                    king = piece
        if king.get_valid_moves(self) == []:
            if self.is_in_check(color):
                output = True
        return output
    
    
    def draw(self, display):
        if self.selected_piece is not None:
            self.get_square_from_pos(self.selected_piece.pos).highlight = True
            for square in self.selected_piece.get_valid_moves(self):
                square.highlight = True
        for square in self.squares:
            square.draw(display)

"""
This code defines the Board class which represents the chessboard and its functionalities. Here's a breakdown of its functionalities:

1. Initialization:

__init__(self, width, height):
Takes the board dimensions (width and height) as arguments.
Calculates the width and height of each square.
Initializes selected_piece to None (no piece selected initially).
Sets the turn to 'white' (white starts the game).
Defines the starting configuration of the pieces on the board using a list of lists representation.
Generates a list of Square objects representing all the squares on the board.
Calls the setup_board method to populate the squares with pieces based on the starting configuration.
2. Methods:

generate_squares(self):

Iterates through all squares on the board and creates a Square object for each one, adding it to a list.
Returns the list of Square objects representing the board.
get_square_from_pos(self, pos):

Takes a square position as a tuple (x, y).
Iterates through the squares on the board and returns the Square object that matches the given position.
get_piece_from_pos(self, pos):

Calls the get_square_from_pos method to get the square at the specified position.
Returns the piece occupying that square, or None if the square is empty.
setup_board(self):

Iterates through the rows and columns of the starting configuration list.
For each piece definition in the configuration:
Extracts the piece type and color from the notation (e.g., "bR" for black rook).
Gets the square object at the corresponding position.
Creates a new piece object of the appropriate type (Rook, Bishop, Knight, Queen, King, or Pawn) based on the notation, passing the position, color, and the Board instance as arguments.
Sets the square's occupying piece to the newly created piece object.
handle_click(self, mx, my):

Converts the mouse click coordinates (mx, my) to board square coordinates.
Gets the Square object clicked.
If no piece is selected:
If a piece occupies the clicked square and it's the current player's turn, sets the selected piece to that piece.
If a piece is selected:
Attempts to move the selected piece to the clicked square. If the move is valid, the piece is moved, the turn changes, and any highlights are cleared.
If the clicked square has a piece and it's the current player's turn, the clicked piece is selected (assuming it belongs to the current player).
is_in_check(self, color, board_change=None):

Checks if the king of the specified color is in check.
Takes an optional board_change argument, which is a temporary move (from, to squares) used to simulate a move and see if it would put the king in check.
If board_change is provided, it temporarily moves the piece and updates the board state accordingly.
Finds the king's position (either from the board_change or by iterating through all pieces).
Iterates through all pieces on the board (excluding the current player's pieces).
For each opposing piece, calls its attacking_squares method to get the squares it can attack.
If any of the attacking squares of an opposing piece matches the king's position, the king is in check, and the method returns True.
If board_change was provided, it restores the original board state.
Returns True if the king is in check, False otherwise.
is_in_checkmate(self, color):

Checks if the specified color is in checkmate.
Iterates through all the squares on the board and finds the king of the specified color.
If the king has no valid moves (considering both moving itself and capturing other pieces), and the king is in check (using is_in_check), then the king is in checkmate, and the method returns True.
Returns True if the king is in checkmate, False otherwise.
draw(self, display):

If a piece is selected"""