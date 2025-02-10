import pygame
# from Lift import *
# from Lift import Lift

NUM_OF_FLOORS = 80
NUM_OF_LIFTS = 4

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 1000

FLOOR_HEIGHT = 80
FLOOR_WIDTH = 120

LIFT_SIZE = FLOOR_HEIGHT, FLOOR_HEIGHT

SPACER_HEIGHT = 7

MARGIN = 10
# width = canvas.get_width()
# height = canvas.get_height()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

red = (255, 0, 0)
light_red = (140, 0, 0)
grey = (128,128,128)
green = (0, 255, 0)
blue = (0, 0, 200)
opaque_grey = (128, 128, 128, 0.5)

# horizontal_floor_posit = width / 2 - 90
# floor_posit = (horizontal_floor_posit, height - 7 - (NUM_OF_FLOORS) * 68)


on_button = False



# import pygame
#
# # Constants
# NUM_OF_FLOORS = 9
# NUM_OF_LIFTS = 4
#
# WINDOW_WIDTH = 1000
# WINDOW_HEIGHT = 700
#
# # Initialize Pygame Window
# CANVAS = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#
# WIDTH = CANVAS.get_width()
# HEIGHT = CANVAS.get_height()
#
# # Colors
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# LIGHT_RED = (140, 0, 0)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 200)
# OPAQUE_GREY = (128, 128, 128, 0.5)
#
# # Floor Settings
# HORIZONTAL_FLOOR_POSIT = WIDTH / 2 - 90
# FLOOR_POSIT = (HORIZONTAL_FLOOR_POSIT, HEIGHT - 7 - (NUM_OF_FLOORS * 68))
# FLOOR_IMG = pygame.image.load('resources/floor_pic.jpg')
# FLOOR_IMG = pygame.transform.scale(FLOOR_IMG, (180, 68))
#
# # Lift Settings
# DEFAULT_IMAGE_POSITION = (160, 640)
# DEFAULT_LIFT_SIZE = (75, 75)
# LIFT_PIC = pygame.image.load('resources/elv.png')
# LIFT_PIC = pygame.transform.scale(LIFT_PIC, DEFAULT_LIFT_SIZE)
#
# # Button State
# ON_BUTTON = False