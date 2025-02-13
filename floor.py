import pygame

from call_button import CallButton
from config import *

def draw_spacer(canvas, top_left, color):
    x, y = top_left
    rect = pygame.Rect(x, y, FLOOR_WIDTH, SPACER_HEIGHT)
    pygame.draw.rect(canvas, color, rect)

class Floor:

    def __init__(self, level, canvas):
        self. canvas = canvas
        self.level = level
        self.button_colour = WHITE
        self.height = self.canvas.get_height() - (MARGIN + (self.level * FLOOR_HEIGHT))
        self.center = HORIZ_CENTER, self.height + FLOOR_HEIGHT // 2
        self.button = CallButton(self.level, self.center)
        self.has_called = False

    def draw(self, canvas, image, spacer_colour=BLACK):
        x = MARGIN
        y = self.height
        canvas.blit(image, (x, y))
        draw_spacer(canvas, (x, y), spacer_colour)
        if self.has_called:
            self.button_colour = GREEN
        self.button.draw_button(canvas, self.button_colour)

    def is_calling(self, pos):
        return self.button.pressed(pos)


    # def allocate_lift(self, canvas, building, window):
    #     dest = canvas.get_height() - self.height
    #     allocated = building.lifts[0]
    #     for lift in building.lifts[1:]:
    #         if lift.call_time + (abs(self.level - lift.final) / 2) < allocated.call_time + (abs(self.level - allocated.final) / 2):
    #             allocated = lift
    #     allocated.upcoming.append(self)
    #     allocated.final = self.level
    #     allocated.travel(canvas, building, window)

