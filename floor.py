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
        self.timer_pos = MARGIN * 2, self.height + FLOOR_HEIGHT // 2 - TIMER_HEIGHT // 2
        self.has_called = False
        self.at_floor = False
        self.time = None
        # self.allocated_lift = None

    def draw(self, canvas, image, spacer_colour=BLACK):
        x = MARGIN
        y = self.height
        canvas.blit(image, (x, y))
        draw_spacer(canvas, (x, y), spacer_colour)
        self.button_colour = GREEN if self.has_called else WHITE
        self.button.draw_button(canvas, self.button_colour)
        if self.time:
            self.draw_timer(canvas)

    def is_calling(self, pos):
        """
        determines if the floor is calling a lift
        :param pos: x, y coordinates of a mouse click
        :return: True if and only if the click was within the bounds of the button
        """
        cx, cy = pos
        x, y = self.center
        if ((cx - x) ** 2 + (cy - y) ** 2) ** 0.5 <= BUTTON_RADIUS:
            return True
        else:
            return False

    def draw_timer(self, canvas):
        x, y = self.timer_pos
        time_left = (self.time - pygame.time.get_ticks()) / 1000
        if time_left >= 0:
            pygame.draw.rect(canvas, BLACK, [x, y, TIMER_WIDTH, TIMER_HEIGHT])
            font = pygame.font.Font(None, 25)
            text = font.render(str(time_left), True, WHITE)
            canvas.blit(text, (x + TEXT_MARGIN, y + TEXT_MARGIN))
        else:
            self.time = None





