import pygame.time

from config import *
from lift import *
from floor import *
from lift import Lift


class Building:
    def __init__(self, num_of_floors, num_of_lifts, canvas):
        self.canvas = canvas
        # current_time = pygame.time.get_ticks()
        self.lifts = [Lift(i, self.canvas, self) for i in range(1,num_of_lifts + 1)]
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
            # if lift.current_floor:
            #     for floor in self.floors:
            #         if floor.level == lift.current_floor:
            #             floor.at_floor = True
            #         else:
            #             floor.at_floor = False
                    # if lift.current_floor:
            #     self.floors[lift.current_floor - 1].at_floor = True
            # else:
            #     self.floors[lift.current_floor - 1].at_floor = False

    def allocate_lift(self, caller):
        # current_time = pygame.time.get_ticks()
        best_arrival_time = float("inf")
        best_lift = self.lifts[0]

        for lift in self.lifts:
            arrival_time = lift.time_when_free + abs(caller - lift.level_when_free) * FLOOR_HEIGHT / PIX_PER_MILISECOND
            if arrival_time < best_arrival_time:
                best_arrival_time = arrival_time
                best_lift = lift
        best_lift.time_when_free = best_arrival_time + LIFT_STOP_TIME
        best_lift.level_when_free = caller
        best_lift.add_stop(caller, self.floors[caller - 1].height)
        self.floors[caller - 1].time = best_arrival_time

    def lift_arrived(self, level):
        self.floors[level - 1].has_called = False
        # self.floors[level - 1].at_floor = True
