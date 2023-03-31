# This section imports all the required libraries
import pygame as pg
import sys
import time
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
lineColor = black

# Board configuration
board = [[None] * 3, [None], * 3, [None] * 3 ]

# Initialize the game
pg.init()

# FPS cap
fps = 30

# Tracks the time
Clock = pg.time.Clock()

# Setting the game window
screen = pg.display.set_mode((width, height + 100),0,32)

# Sets a nametag for the game window
pg.display.set_caption("Tic tac toe!")

# Loads images as python objects
initiatingWindow = pg.image.load("Cover.png")
xImage = pg.image.load("X.png")
yImage = pg.image.load("Y.png")

# Resizes the images
initiatingWindow = pg.transform.scale(initiatingWindow, (width, height + 100))
xImage = pg.transform.scale(xImage, (80,80))
yImage = pg.transform.scale(yImage, (80,80))

# Setting up the game window
def gameWindow():

	# Displaing over the screen
	screen.blit(initiatingWindow, (0,0))

	# Updates the display
	pg.display.update()
	time.sleep(2)
	screen.fill(white)

	# Drawing horizontal lines
	pg.draw.lines(screen, lineColor, (0, height / 3), (width, height / 3),7)
	pg.draw.lines(screen, lineColor, (0, height / 3 * 2), (width, height / 3 * 2),7)

	# Drawing vertical lines
	pg.draw.lines(screen, lineColor, (width / 3, 0), (width / 3, height), 7)
	pg.draw.lines(screen, lineColor, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
	drawStatus()


# Using the draw variable on a function
def drawStatus():
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
	textRect = text.get_rect(center = (width / 2, 500-50))
	screen.blit(text, textRect)
	pg.display.update()












