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
        Initializes a Lift object with its ID, position, and movement properties.

        :param lift_id: Unique identifier for the lift
        :param canvas: The Pygame surface to draw on
        :param callback_function: Function to call when the lift arrives at a floor
        :param wait_time_over: Function to call when the lift's waiting time is over
        """
        self.id = lift_id
        self.height = canvas.get_height() - (MARGIN + LIFT_SIZE[1])  # y coordinate to draw the lift
        self.upcoming = []  # The queue of upcoming stops for the lift
        self.level_when_free = 1
        self.available = True
        self.dest_floor = None  # The lifts current destination floor
        self.dest_height = None  # The lifts current destination y coordinate
        self.x = MARGIN + FLOOR_WIDTH + MARGIN + (LIFT_SIZE[0] * (self.id - 1)) # The lift's x position based on it's number
        self.last_update = None  # Time of last update
        self.waited_time = 0  # Amount of time waited at floor
        self.time_when_free = 0  # Time when this lift will be available
        self.accumulated_error = 0  # Accumulated error due to the rounding in the update function
        self.building_callback = callback_function  # callback function when arrived at floor
        self.wait_time_over = wait_time_over  # callback function when finished two second wait at floor

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
            self.dest_floor, self.dest_height = self.upcoming.pop(
                0)  # Unpacks the floor number and y coordinate from queue
            self.available = False  # Currently busy
            self.last_update = pygame.time.get_ticks()  # Start time of travel

    def arrived(self):
        """
        Handles the event when the lift reaches its destination floor.
        """
        pygame.mixer.music.play() # Plays the ding
        self.waited_time = pygame.time.get_ticks()  # Start time of 2 second wait
        self.building_callback(self.dest_floor, self.upcoming)  # Tells the building that it has arrived at the floor

    def update(self):
        """
        Updates the lift's position and state.
        """
        self.time_when_free = max(pygame.time.get_ticks(),
                                  self.time_when_free)  # Updates the lift's availability time as
        # right now - if there's no upcoming floors
        if not self.available:
            dest_height = self.dest_height  # destination y coordinate
            height = self.height  # Current y coordinate
            if height != dest_height:
                current_time = pygame.time.get_ticks()
                passed_time = current_time - self.last_update
                accurate_dist = passed_time * PIX_PER_MILLISECOND  # Exact amount of pixels it should move (could be a float)
                dist = round(accurate_dist)  # Round the distance to an integer so the lift could move
                self.accumulated_error += accurate_dist - dist  # Accumulate the amount taken off from accurate distance
                if abs(self.accumulated_error) >= 1:                    # When the accumulated error reaches an integer
                    dist += self.accumulated_error // 1                 # It gets added to the distance to travel
                    self.accumulated_error -= self.accumulated_error // 1 # And taken off from the accumulated error - to improve time accuracy
                direction = -1 if height > dest_height else 1 # Determines the direction
                dist = min(dist, abs(dest_height - self.height)) # makes sure it doesn't overshoot the target
                self.height += direction * dist # New height to be drawn at
                self.last_update = current_time # Saves time of last position update
            elif self.waited_time == 0: # If the lift has just arrived at it's destination
                self.arrived()
            else:
                current_time = pygame.time.get_ticks()
                passed_wait_time = current_time - self.waited_time # Determines how much time has passed since it arrived at the floor
                if passed_wait_time >= LIFT_STOP_TIME: # If it has been at the floor the designated wait time
                    self.wait_time_over(self.dest_floor) # callback function that tells the building that the wait time is over
                    self.available = True # Lift is no longer busy
                    self.waited_time = 0
        self.get_next_stop() # Get the lift's next stop

    def draw(self, canvas, image):
        """
        Draws the lift at its correct position.
        :param canvas: The Pygame surface to draw on
        :param image: The image which gets drawn on the canvas
        """
        # x = MARGIN + FLOOR_WIDTH + MARGIN + (LIFT_SIZE[0] * (self.id - 1)) # The lift's x position based on it's number
        # y = self.height # The lift's y coordinate
        canvas.blit(image, (self.x, self.height)) # Draw the lift
