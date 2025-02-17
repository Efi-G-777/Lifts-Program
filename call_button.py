from config import *
from building import *
# from main import building, canvas
from lift import Lift


class CallButton:
    def __init__(self, floor, center):
        self.level = floor
        self.center = center

    def pressed(self, pos):
        cx, cy = pos
        x, y = self.center
        if ((cx - x) ** 2 + (cy - y) ** 2) ** 0.5 <= BUTTON_RADIUS:
            return True
        else: return False


    # def mouse_on_button(self, canvas, x, y):
    #     mouse_pos = pygame.mouse.get_pos()
    #     if (mouse_pos[0] - x) ** 2 + (mouse_pos[1] - y) ** 2 <= BUTTON_RADIUS ** 2:
    #         return True
    #     else: return False


    def draw_button(self, canvas, colour):
        # if self.mouse_on_button(canvas, x, y): #these lines are for making the button grey when hovered over
        #     pygame.draw.circle(canvas, GREY, (x, y), BUTTON_RADIUS)
        # else:
        x, y = self.center
        HORIZ_NUM_MOVE = - 9 if self.level > 9 else - 4
        pygame.draw.circle(canvas, colour, (x, y), BUTTON_RADIUS)
        font = pygame.font.Font(None, 25)
        text = font.render(f'{self.level}', True, RED)
        canvas.blit(text, (x + HORIZ_NUM_MOVE, y + VERT_NUM_MOVE))



            # allocated = self.find_nearest_lift(building.lifts)
            # allocated.travel







    '''def draw_button(self):
        pass
        # on_button = False
        # pygame.draw.circle(canvas, opaque_grey, (self.window_width / 2 + 3, self.window_height + 34 - (self.floor * 75)), 16 )
        if (self.window_width / 2 - 15 <= self.mouse[0] <= self.window_width / 2 +15 and
        self.window_height + 37 - (self.level * 75) - 15 <= self.mouse[1] <= self.window_height + 37 - (self.level * 75) + 15):
            # if self.event == pygame.MOUSEBUTTONDOWN:
            #     pygame.draw.circle(canvas, green, (self.window_width / 2, self.window_height + 37 - (self.floor * 75)),
            #                        15)
            # else:
            pygame.draw.circle(canvas, GREY, (self.window_width / 2, self.window_height + 37 - (self.level * 75)), 15)
            # on_button = True
        else:
            pygame.draw.circle(canvas, white, (self.window_width / 2, self.window_height + 37 - (self.level * 75)), 15)
        canvas.blit(self.text, (self.window_width / 2 - 4, self.window_height + 30 - (self.level * 75)))
        # return on_button'''

