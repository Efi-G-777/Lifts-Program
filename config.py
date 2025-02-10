import pygame
# from Lift import *
# from Lift import Lift

num_of_floors = 9
num_of_lifts = 4

window_width = 1000
window_height = 700


canvas = pygame.display.set_mode((window_width, window_height))

width = canvas.get_width()
height = canvas.get_height()

white = (255, 255, 255)
red = (255, 0, 0)
light_red = (140, 0, 0)
black = (0, 0, 0)
grey = (128,128,128)
green = (0, 255, 0)
blue = (0, 0, 200)
opaque_grey = (128, 128, 128, 0.5)

horizontal_floor_posit = width / 2 - 90
floor_posit = (horizontal_floor_posit, height - 7 - (num_of_floors) * 68)
floor_img = pygame.image.load('resources/floor_pic.jpg')
floor_img = pygame.transform.scale(floor_img,(180, 68))
default_image_position = (160, 640)
default_lift_size = (75, 75)
lift_pic = pygame.image.load('resources/elv.png')
lift_pic = pygame.transform.scale(lift_pic, default_lift_size)

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