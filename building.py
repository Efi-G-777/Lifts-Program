from config import *
from lift import *
from floor import *

class Building:
    def __init__(self, num_of_floors, num_of_lifts):
        self.lifts = [Lift(i) for i in range(num_of_lifts)]
        self.floors = [Floor(i) for i in range(1, num_of_floors + 1)]

    def draw(self, canvas):
        floor_pic = pygame.transform.scale(pygame.image.load('resources/floor_pic.jpg'), (FLOOR_WIDTH, FLOOR_HEIGHT))
        for floor in self.floors[:-1]:
            floor.draw(canvas, floor_pic)
        self.floors[-1].draw(canvas, floor_pic, spacer_color=WHITE)

        lift_pic = pygame.transform.scale(pygame.image.load('resources/elv.png'), LIFT_SIZE)
        for lift in self.lifts:
            lift.draw(canvas, lift_pic)





