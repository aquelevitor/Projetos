# This section imports all the required libraries
import time
import sys
import pygame as pg
from pygame.locals import *

# Variable to store 'x' or 'o'
XO = 'x'

# Storing the winner's value
winner = None

# Variable to check if the game is a draw
draw = None

# Game window configuration
width = 800
height = 600

# Background color and line color
white = (255,255,255)
black = (0,0,0)

# Color of the line that divides the board sections
line_color = black

# Board configuration
board = [[None] * 3, [None], * 3, [None] * 3 ]

# Initialize the game
pg.init()

# FPS cap
fps = 30

# Tracks the time
CLOCK = pg.time.Clock()

# Setting the game window
screen = pg.display.set_mode((width, height + 100),0,32)

# Sets a nametag for the game window
pg.display.set_caption("Tic tac toe!")

# Loads images as python objects
initiating_window = pg.image.load("Cover.png")
x_image = pg.image.load("X.png")
y_image = pg.image.load("Y.png")

# Resizes the images
initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
x_image = pg.transform.scale(x_image, (80,80))
y_image = pg.transform.scale(y_image, (80,80))

# Setting up the game window
def game_window():

	# Displaing over the screen
	screen.blit(initiating_window, (0,0))

	# Updates the display
	pg.display.update()
	time.sleep(2)
	screen.fill(white)

	# Drawing horizontal lines
	pg.draw.lines(screen, line_color, (0, height / 3), (width, height / 3),7)
	pg.draw.lines(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2),7)

	# Drawing vertical lines
	pg.draw.lines(screen, line_color, (width / 3, 0), (width / 3, height), 7)
	pg.draw.lines(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
	draw_status()


# Using the draw variable on a function
def draw_status():
	global draw

	if winner is None:
		message = XO.upper() + "'s Turn"
	else:
		message = winner.upper() + " Won!"
	if draw:
		message = "That's a Draw!!"

	# Setting up a font object
	font = pg.font.Font(None,30)

	# Choosing some properties for the font
	text = font.render(message, 1, (white))

	# Copying the rendered message onto the board
	# Creating a small block at the bottom of main display
	screen.fill(black, (0,400,500,100))
	text_rect = text.get_rect(center = (width / 2, 500-50))
	screen.blit(text, text_rect)
	pg.display.update()

# Creates a function to check wins
def check_win():
	global board, winner, draw

	# Checking for winner on rows
	for row in range(0,3):
		if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
			winner = board[row][0]
			pg.draw.line(screen, (250,0,0),
						(0, (row + 1) * height / 3 - height / 6),
						(width, (row + 1) * height / 3 - height / 6), 4)

		break

	# Checking for winner on columns
	for col in range(0,3):
		if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
			winner = board[0][col]
			pg.draw.line(screen, (250,0,0),
								 ((col + 1) * width / 3 - width / 6, 0),
								 ((col + 1) * width / 3 - width / 6, height), 4)
		break

	# Checking for diagonal winners
	if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
		
		# Game won diagonally from left to right
		winner = board[0][0]
		pg.draw.line(screen, (250,70,70), (50,50), (350,350), 4)

	if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):

		# Game won diagonally from right to left
		winner = board[0][2]
		pg.draw.line(screen, (250,70,70), (350,50), (50,350), 4)

	if (all([all(row) for row in board]) and winner is None):
		draw = True

	draw_status()	









