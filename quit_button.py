import pygame.mouse
import sys
from config import *

# Initialising pygame
pygame.init()

# CREATING CANVAS
canvas = pygame.display.set_mode((window_width, window_height))

# TITLE OF CANVAS
pygame.display.set_caption("Non-Resizable Board")

# pygame.display.set_icon(image)

font = pygame.font.SysFont('Corbel', 25)
text = font.render('Quit', True, white)

width = canvas.get_width()
height = canvas.get_height()

run = True
while run:
    canvas.fill(white)
    mouse = pygame.mouse.get_pos()

    if (width / 2 <= mouse[0] <= width/2 + 140 and
        height / 2 <= mouse[1] <= height / 2 + 40):
        pygame.draw.rect(canvas, light_red, [width / 2, height / 2, 140, 40])
    else:
        pygame.draw.rect(canvas, red, [width / 2, height / 2, 140, 40])

    canvas.blit(text, (width / 2 + 50, height / 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (width / 2 <= mouse[0] <= width/2 + 140 and
        height / 2 <= mouse[1] <= height / 2 + 40):
                run = False

    pygame.display.update()
