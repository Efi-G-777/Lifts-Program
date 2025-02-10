import pygame

from config import *

def draw_spacer(canvas, top_left, color):
    x, y = top_left
    rect = pygame.Rect(x, y, FLOOR_WIDTH, SPACER_HEIGHT)
    pygame.draw.rect(canvas, color, rect)

class Floor:

    def __init__(self, level):
        self.level = level

    def draw(self, canvas, image, spacer_color=BLACK):
        x = MARGIN
        y = canvas.get_height() - MARGIN - FLOOR_HEIGHT * (self.level)
        canvas.blit(image, (x, y))
        draw_spacer(canvas, (x, y), spacer_color)