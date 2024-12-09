import pygame
import tkinter as tk
import threading
from time import sleep
from data.classes.Board import Board


pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	display.fill('white')
	board.draw(display)
	pygame.display.update()

def show_checkmate_alert(color):
    """
    Creates a visual and audio alert for checkmate.

    Args:
        color (str): The color of the king that is in checkmate.
    """

    # Create a separate window for the alert (consider customization for aesthetics)
    alert_window = tk.Tk()
    alert_window.title("Checkmate!")
    alert_window.geometry("300x100")  # Adjustable window size

    # Create a red blinking label for checkmate state
    checkmate_label = tk.Label(alert_window, text="Checkmate! " + color.capitalize() + " Loses", fg="red")
    checkmate_label.pack()

    def blink_label():
        while True:
            current_fg = checkmate_label.cget("fg")
            checkmate_label.config(fg="black" if current_fg == "red" else "red")
            sleep(0.5)  # Adjust blink speed

    # Start blinking the label concurrently
    blink_thread = threading.Thread(target=blink_label, daemon=True)
    blink_thread.start()

    # Play an audio alert (placeholder for actual sound playing code)
    # Place your audio playback code here (e.g., using a sound library or platform-specific methods)
    # For example (replace with your preferred audio playback method):
    #   play_sound("path/to/checkmate.wav")

    alert_window.mainloop()  # Display the alert window


if __name__ == '__main__':
	running = True
	while running:
		mx, my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			# Quit the game if the user presses the close button
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN: 
       			# If the mouse is clicked
				if event.button == 1:
					board.handle_click(mx, my)
		if board.is_in_checkmate('black'): # If black is in checkmate
			print('White wins!')
			running = False
		elif board.is_in_checkmate('white'): # If white is in checkmate
			print('Black wins!')
			running = False
		# Draw the board
		draw(screen)

"""
This code initializes a basic graphical interface for a chess game using the Pygame library. Here's a breakdown of how it works:

1. Imports and Initialization:

pygame.init(): Initializes the Pygame library.
Board class: Imports the Board class likely defined elsewhere, which represents the chessboard logic and functionalities.
WINDOW_SIZE: Defines the window size for the chessboard display (600x600 pixels).
screen: Creates the game window using pygame.display.set_mode with the defined size.
board: Creates an instance of the Board class, passing the window dimensions likely to set up the board representation.
2. Drawing Function (draw(display)):

Fills the screen with white color.
Calls the draw method of the board object, likely responsible for drawing the squares, pieces, and other visual elements of the board onto the display (display).
Updates the Pygame display to reflect the changes.
3. Main Loop:

running flag: Set to True to keep the game loop running.
The loop continues as long as running is True.
Event Handling:
Gets the current mouse position (mx, my).
Iterates through all pygame events in the queue:
If the event type is pygame.QUIT, the user closed the window, and the loop is terminated.
If the event type is pygame.MOUSEBUTTONDOWN (mouse click):
If the left mouse button is clicked (event.button == 1), calls the board.handle_click(mx, my) method, likely responsible for handling user clicks on the chessboard squares (e.g., selecting pieces, making moves).
Checks for checkmate:
If board.is_in_checkmate('black') returns True, black is in checkmate, so "White wins!" is printed, and the loop is terminated.
Similarly, for white being in checkmate.
Drawing:
Calls the draw function to update the display with the current board state."""
