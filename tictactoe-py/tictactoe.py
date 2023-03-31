# This section imports all the required libraries
import pygame as pg
import sys
import time
from pygame.locals import *

# Variable to store 'x' or 'o'
XO = 'x'

# Storing the winner's value
winner = None

# To check if the game is a draw
draw = None

# Game window configuration
width = 800
height = 600

# Background color
white = (255,255,255)

# Color of the line that divides the board sections
lineColor = (0,0,0)

# Board configuration
board = [[None] * 3, [None], * 3, [None] * 3]





