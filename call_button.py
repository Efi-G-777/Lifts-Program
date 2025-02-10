from config import *
# from start import font


class CallButton:
    def __init__(self, floor):
        self.floor = floor
        self.window_width = canvas.get_width()
        self.window_height = canvas.get_height()
        self.font = pygame.font.SysFont('Corbel', 25)
        self.text = self.font.render(f'{self.floor}', True, red)
        self.mouse = pygame.mouse.get_pos()
        # self.event = pygame.event.get()



    def draw_button(self):
        # on_button = False
        # pygame.draw.circle(canvas, opaque_grey, (self.window_width / 2 + 3, self.window_height + 34 - (self.floor * 75)), 16 )
        if (self.window_width / 2 - 15 <= self.mouse[0] <= self.window_width / 2 +15 and
        self.window_height + 37 - (self.floor * 75) - 15 <= self.mouse[1] <= self.window_height + 37 - (self.floor * 75) + 15):
            # if self.event == pygame.MOUSEBUTTONDOWN:
            #     pygame.draw.circle(canvas, green, (self.window_width / 2, self.window_height + 37 - (self.floor * 75)),
            #                        15)
            # else:
            pygame.draw.circle(canvas, grey, (self.window_width / 2, self.window_height + 37 - (self.floor * 75)), 15)
            on_button = True
        else:
            pygame.draw.circle(canvas, white, (self.window_width / 2, self.window_height + 37 - (self.floor * 75)), 15)
        canvas.blit(self.text, (self.window_width / 2 - 4, self.window_height + 30 - (self.floor * 75)))
        # return on_button



def initialise_buttons(floors):
    buttons_coords = []
    buttons_list = []
    for i in range(1, floors + 1):
        buttons_list.append(CallButton(i))
        buttons_coords.append((width / 2, height + 37 - (i * 75)))
    return buttons_list, buttons_coords

# print((initialise_buttons(num_of_floors))[0])

def make_buttons(floors):
    buttons_list = initialise_buttons(floors)[0]
    for button in buttons_list:
        button.draw_button()
