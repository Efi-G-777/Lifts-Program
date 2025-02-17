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


    def draw_button(self, canvas, colour):
        x, y = self.center
        horiz_num_move = - 9 if self.level > 9 else - 4
        pygame.draw.circle(canvas, colour, (x, y), BUTTON_RADIUS)
        font = pygame.font.Font(None, 25)
        text = font.render(f'{self.level}', True, RED)
        canvas.blit(text, (x + horiz_num_move, y + VERT_NUM_MOVE))
