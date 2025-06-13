# /* Square.py
import pygame

# Tile creator
class Square:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = x * width
        self.abs_y = y * height
        self.abs_pos = (self.abs_x, self.abs_y)
        self.pos = (x, y)
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        """if (x + y) % 2 == 0:
            self.color = 'light'
        else:
            self.color = 'dark
        'light' if ... else 'dark': This is the ternary operator that assigns 
        'light' if the condition is True (the sum is even), and 
        'dark' if the condition is False (the sum is odd)."""
        self.draw_color = (220, 208, 194) if self.color == 'light' else (53, 53, 53)
        """if self.color == 'light':
            self.draw_color = (220, 208, 194) : light beige color
        else:
            self.draw_color = (53, 53, 53) :  dark grey color"""
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)
        """if self.color == 'light':
            self.highlight_color = (100, 249, 83) : Vibrant Green. It's hexadecimal code is #64F953.
        else:
            self.highlight_color = (0, 228, 10) : Vibrant Green. It's hexadecimal code is #00E40A."""
        self.occupying_piece = None
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )

    # get the formal notation of the tile
    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)

    def draw(self, display):
        # configures if tile should be light or dark or highlighted tile
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)
        # adds the chess piece icons
        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)

"""
This code defines the Square class, which represents a single square on the chessboard. Here's a breakdown of its functionalities:

1. Initialization:

__init__(self, x, y, width, height):
Takes the square's coordinates (x, y) and its dimensions (width and height) as arguments.
Calculates the absolute position based on coordinates and dimensions.
Determines the color of the square based on its position (light squares for even sum of x and y, dark squares for odd sum).
Sets drawing colors based on the square's color (light or dark).
Initializes attributes for occupying piece, square coordinates in standard chess notation format, highlight state, and a pygame rectangle object representing the square on the display.
2. Methods:

get_coord(self):

Converts the square's coordinates (x, y) to standard chess notation (e.g., "e5").
draw(self, display):

Fills the square on the display with its corresponding color (light, dark, or highlight).
If a piece is occupying the square, its image is centered and drawn on top of the square's color."""