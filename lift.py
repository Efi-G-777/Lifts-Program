import pygame.time
import pygame.mixer
from config import *
from building import *


class Lift:
    """
       Represents a lift in the building that moves between floors.
    """

    def __init__(self, lift_id, canvas, callback_function, wait_time_over):
        """
        Initializes a Lift object.

        :param lift_id: Unique identifier for the lift
        :param canvas: The Pygame surface to draw on
        :param callback_function: Function to call when the lift arrives at a floor
        :param wait_time_over: Function to call when the lift's waiting time is over
        """
        self.id = lift_id
        # self.canvas = canvas
        self.current_floor = 1
        self.height = canvas.get_height() - (MARGIN + LIFT_SIZE[1])
        self.call_time = 0
        self.upcoming = []
        self.level_when_free = 1
        self.available = True
        self.dest_floor = 1
        self.dest_height = None
        self.last_update = 0
        self.waited_time = 0
        self.time_when_free = 0
        self.accumulated_error = 0
        self.building_callback = callback_function
        self.wait_time_over = wait_time_over

    def add_stop(self, floor, height):
        """
        Adds a floor to the list of upcoming stops for the lift.

        :param floor: Floor number
        :param height: Height of the floor
        """
        self.upcoming.append((floor, height))

    def get_next_stop(self):
        """
        Retrieves the next stop from the upcoming stops list.
        """
        if self.available and self.upcoming:
            self.dest_floor, self.dest_height = self.upcoming.pop(0)
            self.available = False
            self.last_update = pygame.time.get_ticks()

    def arrived(self):
        """
        Handles the event when the lift reaches its destination floor.
        """
        pygame.mixer.music.play()
        self.waited_time = pygame.time.get_ticks()
        self.building_callback(self.dest_floor, self.upcoming)


    def update(self):
        """
        Updates the lift's position and state.
        """
        self.time_when_free = max(pygame.time.get_ticks(), self.time_when_free)
        if not self.available:
            dest_height = self.dest_height
            height = self.height
            if height != dest_height:
                self.current_floor = None
                current_time = pygame.time.get_ticks()
                passed_time = current_time - self.last_update
                accurate_dist = passed_time * PIX_PER_MILLISECOND
                dist = round(accurate_dist)
                self.accumulated_error += accurate_dist - dist
                if abs(self.accumulated_error) >= 1:
                    dist += self.accumulated_error // 1
                    self.accumulated_error -= self.accumulated_error // 1
                direction = -1 if height > dest_height else 1
                dist = min(dist, abs(dest_height - self.height))
                self.height += direction * dist
                self.last_update = current_time
            elif self.waited_time == 0:
                self.arrived()
            else:
                current_time = pygame.time.get_ticks()
                passed_wait_time = current_time - self.waited_time
                if passed_wait_time >= LIFT_STOP_TIME:
                    self.wait_time_over(self.dest_floor)
                    self.available = True
                    self.waited_time = 0
        self.get_next_stop()

    def draw(self, canvas, image):
        """
        Draws the lift at its correct position.
        :param canvas: The Pygame surface to draw on
        :param image: The image which gets drawn on the canvas
        """
        x = MARGIN + FLOOR_WIDTH + MARGIN + (LIFT_SIZE[0] * (self.id - 1))
        y = self.height
        canvas.blit(image, (x, y))
