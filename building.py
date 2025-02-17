import pygame.time
from config import *
from lift import *
from floor import *
from lift import Lift


class Building:
    def __init__(self, num_of_floors, num_of_lifts, canvas):
        self.canvas = canvas
        # current_time = pygame.time.get_ticks()
        self.lifts = [Lift(i, self.canvas, self.lift_arrived, self.wait_time_over) for i in range(1,num_of_lifts + 1)]
        self.floors = [Floor(i, self.canvas) for i in range(1, num_of_floors + 1)]

    def draw(self, canvas):
        # floor_pic = pygame.transform.scale(pygame.image.load('resources/floor_pic.jpg'), (FLOOR_WIDTH, FLOOR_HEIGHT))
        for floor in self.floors[:-1]:
            floor.draw(canvas, FLOOR_PIC)
        self.floors[-1].draw(canvas, FLOOR_PIC, spacer_colour=WHITE)

        # lift_pic = pygame.transform.scale(pygame.image.load('resources/elv.png'), LIFT_SIZE)
        for lift in self.lifts:
            lift.draw(canvas, LIFT_PIC)

    def update(self, pos):
        if pos:
            for floor in self.floors:
                if floor.is_calling(pos):
                    if not floor.has_called:
                        if not floor.at_floor:
                            self.allocate_lift(floor.level)
                            floor.has_called = True
        for lift in self.lifts:
            lift.update()

    def allocate_lift(self, caller):
        best_arrival_time = float("inf")
        best_lift = self.lifts[0]

        for lift in self.lifts:
            arrival_time = lift.time_when_free + abs(caller - lift.level_when_free) * FLOOR_HEIGHT / PIX_PER_MILLISECOND
            if arrival_time < best_arrival_time:
                best_arrival_time = arrival_time
                best_lift = lift
        best_lift.time_when_free = best_arrival_time + LIFT_STOP_TIME
        best_lift.level_when_free = caller
        best_lift.add_stop(caller, self.floors[caller - 1].height)
        self.floors[caller - 1].time = best_arrival_time

    def lift_arrived(self, level, upcoming_list):
        self.floors[level - 1].has_called = False
        self.floors[level - 1].at_floor = True
        last_floor = level
        arrival_time = pygame.time.get_ticks()
        for floor in upcoming_list:
            arrival_time += abs(last_floor - floor[0]) * MILLISECONDS_PER_FLOOR + LIFT_STOP_TIME
            self.floors[floor[0] - 1].time = arrival_time
            last_floor = floor[0]

    def wait_time_over(self, level):
        self.floors[level - 1].at_floor = False


