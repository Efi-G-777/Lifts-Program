from config import *
from lift import *
from floor import *

class Building:
    def __init__(self, num_of_floors, num_of_lifts, canvas):
        self.canvas = canvas
        self.lifts = [Lift(i, self.canvas) for i in range(1,num_of_lifts + 1)]
        self.floors = [Floor(i, self.canvas) for i in range(1, num_of_floors + 1)]

    def draw(self, canvas):
        # floor_pic = pygame.transform.scale(pygame.image.load('resources/floor_pic.jpg'), (FLOOR_WIDTH, FLOOR_HEIGHT))
        for floor in self.floors[:-1]:
            floor.draw(canvas, FLOOR_PIC)
        self.floors[-1].draw(canvas, FLOOR_PIC, spacer_colour=WHITE)

        # lift_pic = pygame.transform.scale(pygame.image.load('resources/elv.png'), LIFT_SIZE)
        # y = canvas.get_height() - MARGIN - LIFT_SIZE[1]
        for lift in self.lifts:
            lift.draw(canvas, LIFT_PIC)

    def update(self, pos):
        if pos:
            for floor in self.floors:
                if floor.is_calling(pos):
                    self.allocate_lift(floor)
                    # floor.button_colour = GREEN
                    floor.has_called = True
        for lift in self.lifts:
            lift.move()

    def allocate_lift(self, caller):
        nearest = self.lifts[0]
        for lift in self.lifts[1:]:
            if lift.call_time + (abs(caller.level - lift.final) / 2) < nearest.call_time + (
                    abs(caller.level - nearest.final) / 2):
                nearest = lift
        travel_time = (abs(caller.level - nearest.final) / 2) + 2
        nearest.add_stop(caller, travel_time)
        # nearest.upcoming.append(caller)

    '''def check_button(self, canvas,  mouse, building, window):
        if BUTTON_LEFT_EDGE <= mouse[0] <= BUTTON_RIGHT_EDGE:
            for floor in self.floors:
                if canvas.get_height() - floor.center - BUTTON_RADIUS <= mouse[1] <= canvas.get_height() - floor.center + BUTTON_RADIUS:
                    # pygame.draw.circle(canvas, RED, (10, canvas.get_height() - 10), 10)
                    self.allocate_lift(canvas, floor, building, window)

    def allocate_lift(self, canvas, caller, building, window):
        nearest = self.lifts[0]
        for lift in self.lifts[1:]:
            if lift.call_time + (abs(caller.level - lift.final) / 2) < nearest.call_time + (abs(caller.level - nearest.final) / 2):
                nearest = lift
        nearest.upcoming.append(caller)
        # nearest.travel(canvas, building, window)'''




