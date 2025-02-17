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
        self.at_floor = False
        self.time = None
        # self.lift_state = 1
        # self.allocated_lift = None

    def draw(self, canvas, image, spacer_colour=BLACK):
        x = MARGIN
        y = self.height
        canvas.blit(image, (x, y))
        draw_spacer(canvas, (x, y), spacer_colour)
        self.button_colour = GREEN if self.has_called else WHITE
        self.button.draw_button(canvas, self.button_colour)
        if self.time:
            self.start_timer(canvas)

    def is_calling(self, pos):
        return self.button.pressed(pos)

    def start_timer(self, canvas):
        x, y = self.center
        time_left = (self.time - pygame.time.get_ticks()) / 1000
        if time_left >= 0:
            # pygame.draw.circle(canvas, WHITE, (x, y), BUTTON_RADIUS)
            pygame.draw.rect(canvas, BLACK, [x - 70, y - 15, 50, 30])
            font = pygame.font.Font(None, 25)
            text = font.render(str(time_left), True, WHITE)
            canvas.blit(text, (x - 65, y - 10))
        else:
            self.time = None


    # def allocate_lift(self, canvas, building, window):
    #     dest = canvas.get_height() - self.height
    #     allocated = building.lifts[0]
    #     for lift in building.lifts[1:]:
    #         if lift.call_time + (abs(self.level - lift.final) / 2) < allocated.call_time + (abs(self.level - allocated.final) / 2):
    #             allocated = lift
    #     allocated.upcoming.append(self)
    #     allocated.final = self.level
    #     allocated.travel(canvas, building, window)



 # if self.allocated_lift:
        #     if self.allocated_lift.height == self.height:
        #         self.button_colour = GREEN
        #     else:
        #         self.button_colour = BLUE
        # else:
        #     self.button_colour = WHITE
        # if self.lift_state == 2:
        #     self.button_colour = GREEN
        # elif self.lift_state == 3:
        #     self.button_colour = BLUE
        # else:
        #     self.button_colour = WHITE
