# from config import *
import pygame.draw

from building import *
from lift import *
from call_button import *

# Initialising pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(DING_SOUND)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Lift Program")

canvas_height = max(2 * MARGIN + FLOOR_HEIGHT * NUM_OF_FLOORS, WINDOW_HEIGHT)
canvas = pygame.Surface((WINDOW_WIDTH, canvas_height))

building = Building(NUM_OF_FLOORS, NUM_OF_LIFTS, canvas)

run = True

while run:
    pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # building.check_button(canvas, pos, building, window)
    canvas.fill(WHITE)
    building.draw(canvas)
    building.update(pos)
    window.blit(canvas, (0, 0))

    pygame.display.flip()
