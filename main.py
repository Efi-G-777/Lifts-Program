# from config import *
import pygame.draw
from building import *
from lift import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(DING_SOUND)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Lift Program")

canvas_height = max(2 * MARGIN + FLOOR_HEIGHT * NUM_OF_FLOORS, WINDOW_HEIGHT)
canvas = pygame.Surface((WINDOW_WIDTH, canvas_height))

scroll_speed  = 20
scroll_y = canvas_height - WINDOW_HEIGHT

building = Building(NUM_OF_FLOORS, NUM_OF_LIFTS, canvas)

run = True

while run:
    pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # mouse left
                pos = pygame.mouse.get_pos()
                x, y = pos
                pos = x, y + scroll_y
            elif event.button == 4: # mouse wheel up
                scroll_y -= scroll_speed
            elif event.button == 5: # mouse wheel down
                scroll_y += scroll_speed
            scroll_y = max(0, min(canvas_height - WINDOW_HEIGHT, scroll_y))

    canvas.fill(WHITE)
    building.draw(canvas)
    building.update(pos)
    window.blit(canvas, (0, -scroll_y))

    pygame.display.flip()
