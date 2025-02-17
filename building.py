import pygame.time
from config import *
from lift import *
from floor import *
from lift import Lift


class Building:
    """
    Represents a building with multiple floors and lifts.
    """
    def __init__(self, num_of_floors, num_of_lifts, canvas):
        """
        Initializes the Building with floors and lifts.

        :param num_of_floors: Number of floors in the building
        :param num_of_lifts: Number of lifts in the building
        :param canvas: The Pygame surface to draw on
        """
        self.canvas = canvas
        self.lifts = [Lift(i, self.canvas, self.lift_arrived, self.wait_time_over) for i in range(1,num_of_lifts + 1)]
        self.floors = [Floor(i, self.canvas) for i in range(1, num_of_floors + 1)]

    def draw(self, canvas):
        """
        Draws floors and lifts on the canvas.
        :param canvas: The Pygame surface to draw on
        """
        for floor in self.floors[:-1]:
            floor.draw(canvas, FLOOR_PIC)                           #iterates over all the floors and draws them -
        self.floors[-1].draw(canvas, FLOOR_PIC, spacer_colour=WHITE) #except for the last one which is drawn
                                                                    #separately with a different spacer colour
        for lift in self.lifts:
            lift.draw(canvas, LIFT_PIC)

    def update(self, pos):
        """
        Updates the state of the building, checking for floor calls and updating lifts.

        :param pos: Position of mouse click for floor calls
        """
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
        """
        Allocates the best available lift to the calling floor.

        :param caller: Floor number that requested the lift
        """
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
        """
        Handles the event when a lift arrives at a floor.

        :param level: The floor number where the lift arrives
        :param upcoming_list: The list of upcoming stops for the lift
        """
        self.floors[level - 1].has_called = False
        self.floors[level - 1].at_floor = True
        last_floor = level
        arrival_time = pygame.time.get_ticks()
        for floor in upcoming_list:
            arrival_time += abs(last_floor - floor[0]) * MILLISECONDS_PER_FLOOR + LIFT_STOP_TIME
            self.floors[floor[0] - 1].time = arrival_time
            last_floor = floor[0]

    def wait_time_over(self, level):
        """
           Handles the event when a floor's wait time is over.

           :param level: The floor number whose wait time has ended
        """
        self.floors[level - 1].at_floor = False


