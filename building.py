from config import *

class Building:
    def __init__(self, floors):
        self.height = floors
        self.window_width = canvas.get_width()
        self.window_height = canvas.get_height()

    def build(self):
        for i in range(1, self.height + 1):
            canvas.blit(floor_img, (self.window_width / 2 - 90, self.window_height - (i * 75)))
            pygame.draw.rect(canvas, black, [self.window_width / 2 - 90, self.window_height - 7 - (i * 75), 180, 7])
        pygame.draw.rect(canvas, white, [self.window_width / 2 - 90, self.window_height - 7 - (self.height * 75), 180, 7])
        pygame.draw.rect(canvas, white, [self.window_width / 2 - 90, self.window_height - 7, 180, 7])

a = Building(num_of_floors)




