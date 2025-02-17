import pygame.time
import pygame.mixer
from config import *
from building import *


class Lift:

    def __init__(self, lift_id, canvas, building):
        self.id = lift_id
        self.canvas = canvas
        self.current_floor = 1
        self.height = self.canvas.get_height() - (MARGIN + LIFT_SIZE[1])
        self.call_time = 0
        self.upcoming = []
        self.level_when_free = 1
        self.available = True
        self.dest_floor = 1
        self.dest_height = None
        self.last_update = 0
        self.waited_time = 0
        self.my_building = building
        self.time_when_free = 0
        self.accumulated_error = 0


    def add_stop(self, floor, height):
        self.upcoming.append((floor, height))

    def get_next_stop(self):
        if self.available and self.upcoming:
            # self.current_floor = None
            self.dest_floor, self.dest_height = self.upcoming.pop(0)
            self.available = False
            self.last_update = pygame.time.get_ticks()

    def arrived(self):
        pygame.mixer.music.play()
        self.waited_time = pygame.time.get_ticks()
        self.my_building.lift_arrived(self.dest_floor)
        # self.current_floor = self.dest_floor

    def update(self):
        self.time_when_free = max(pygame.time.get_ticks(), self.time_when_free)
        if not self.available:
            dest_height = self.dest_height
            height = self.height
            if height != dest_height:
                self.current_floor = None
                current_time = pygame.time.get_ticks()
                passed_time = current_time - self.last_update
                accurate_dist = passed_time * PIX_PER_MILISECOND
                dist = round(accurate_dist)
                self.accumulated_error += accurate_dist - dist
                if abs(self.accumulated_error) >= 1:
                    dist += self.accumulated_error // 1
                    self.accumulated_error -= self.accumulated_error // 1
                direction = -1 if height > dest_height else 1
                # self.call_time -= (abs(direction) * min(dist, abs(dest_height - height))) / 160
                dist = min(dist, abs(dest_height - self.height))
                self.height += direction * dist
                self.last_update = current_time
            elif self.waited_time == 0:
                self.arrived()
            else:
                current_time = pygame.time.get_ticks()
                passed_wait_time = current_time - self.waited_time
                if passed_wait_time >= LIFT_STOP_TIME:
                    self.available = True
                    self.waited_time = 0
        self.get_next_stop()




    def draw(self, canvas, image):
        x = MARGIN + FLOOR_WIDTH + MARGIN + (LIFT_SIZE[0] * (self.id - 1))
        y = self.height
        canvas.blit(image, (x, y))




