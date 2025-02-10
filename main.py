# from config import *
import pygame.draw

from building import *
from lift import *
from call_button import *

# Initialising pygame
pygame.init()



# TITLE OF CANVAS
pygame.display.set_caption("Lift Program")


run = True
while run:
    # width = canvas.get_width()
    # height = canvas.get_height()
    mouse = pygame.mouse.get_pos()
    canvas.fill(blue)
    a.build()
    initialise_lifts(num_of_lifts)
    make_buttons(num_of_floors)
    # pygame.draw.circle(canvas, red, (300, 200), 75)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if on_button:
                pygame.draw.circle(canvas, red, (0, 0), 25)
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
