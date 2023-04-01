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
width = 400
height = 400

# Background color and line color
white = (255,255,255)
black = (0,0,0)

# Color of the line that divides the board sections
line_color = black

# Board configuration
board = [[None] * 3, [None] * 3, [None] * 3 ]

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
o_image = pg.image.load("O.png")

# Resizes the images
initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
x_image = pg.transform.scale(x_image, (80,80))
o_image = pg.transform.scale(o_image, (80,80))

# Setting up the game window
def game_window():

	# Displaing over the screen
	screen.blit(initiating_window, (0,0))

	# Updates the display
	pg.display.update()
	time.sleep(2)
	screen.fill(white)

	# Drawing horizontal lines
	pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3),7)
	pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2),7)

	# Drawing vertical lines
	pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
	pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
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
		if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
			winner = board[row][0]
			pg.draw.line(screen, (250,0,0),
						(0, (row + 1) * height / 3 - height / 6),
						(width, (row + 1) * height / 3 - height / 6), 4)

		break

	# Checking for winner on columns
	for col in range(0,3):
		if ((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
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

# Draws X or O
def drawXO(row, col):
	global board, XO

	# For the first row, the image should be pasted at a x coordinate
	# of 30 from the left margin
	if row == 1:
		posx = 30

	# For the second row, the image should be pasted at a x coordinate
	# of 30 from the game line
	if row == 2:

		# Margin or width / 3 + 30 from
		# the left margin of the window
		posx = width / 3 + 30

	if row == 3:
		posx = width / 3 * 2 + 30

	if col == 1:
		posy = 30

	if col == 2:
		posy = height / 3 + 30

	if col == 3:
		posy = height / 3 * 2 + 30

	# Setting up the required board values to display
	board[row - 1][col - 1] = XO

	if(XO == 'x'):

		# Pasting x_image over the screen at a coordinate position of
		# (posy, posx) defined in the code above
		screen.blit(x_image, (posy, posx))
		XO = 'o'

	else:
		screen.blit(o_image, (posy, posx))
		XO = 'x'
	pg.display.update()

def user_click():
	# Mouse coordinates
	x, y = pg.mouse.get_pos()

	# Get column of mouse click (1 - 3)
	if (x < width / 3):
		col = 1

	elif (x < width / 3 * 2):
		col = 2

	elif (x < width):
		col = 3

	else:
		col = None

	# Get row of the mouse click (1 - 3)
	if (y < height / 3):
		row = 1

	elif (y < height / 3 * 2):
		row = 2

	elif (y < height):
		row = 3

	else:
		row = None

	# After getting the right coordinates
	# we need to draw the images at the right position
	if(row and col and board[row-1][col-1] is None):
		global XO

		drawXO(row,col)
		check_win()

# Creates a function to reset all parameters and restart the game
def reset_game():
	global board, winner, XO, draw
	time.sleep(2)
	XO = 'x'
	draw = False
	game_window()
	winner = None
	board = [[None] * 3, [None] * 3, [None] * 3]

game_window()

# Game loop
while True:
	for event in pg.event.get():
		if event.type == QUIT:
			pg.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			user_click()

			if winner or draw:
				reset_game()
	
	pg.display.update()
	CLOCK.tick(fps)

		











