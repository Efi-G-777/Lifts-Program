import pygame.time
import pygame.mixer
from config import *

class Lift:

    def __init__(self, lift_id, canvas):
        self.id = lift_id
        self.canvas = canvas
        self.current_floor = 1
        self.height = self.canvas.get_height() - (MARGIN + LIFT_SIZE[1])
        self.call_time = 0
        self.upcoming = []
        self.final = 1
        self.available = True
        self.dest_height = None
        self.last_update = 0
        self.wait_time = 0


    def add_stop(self, floor, travel_time):
        self.upcoming.append(floor)
        self.call_time += travel_time
        self.final = floor.level

    def get_next_stop(self):
        if self.available and self.upcoming:
            self.dest_height = self.upcoming.pop(0).height
            self.available = False
            self.last_update = pygame.time.get_ticks()

    def arrived(self):
        pygame.mixer.music.play()
        self.wait_time = pygame.time.get_ticks()

    def move(self):
        if not self.available:
            dest_height = self.dest_height
            height = self.height
            if height != dest_height:
                current_time = pygame.time.get_ticks()
                passed_time = current_time - self.last_update
                dist = round(passed_time * PIX_PER_MILISECOND)
                direction = -1 if height > dest_height else 1
                self.height += direction * min(dist, abs(dest_height - height))
                self.last_update = current_time
            elif self.wait_time == 0:
                self.arrived()
            else:
                current_time = pygame.time.get_ticks()
                passed_wait_time = current_time - self.wait_time
                if passed_wait_time >= LIFT_STOP_TIME:
                    self.available = True
                    self.wait_time = 0
        self.get_next_stop()




    def draw(self, canvas, image):
        x = MARGIN + FLOOR_WIDTH + MARGIN + (LIFT_SIZE[0] * (self.id - 1))
        y = self.height
        canvas.blit(image, (x, y))


    '''def travel(self, canvas, building, window):
        # y = MARGIN + (self.current_floor * FLOOR_HEIGHT)
        if self.upcoming:
            next_floor = self.upcoming.pop(0)
            self.call_time += abs(next_floor.level - self.current_floor) / 2 + 2
            step = 2 if next_floor.level > self.current_floor else - 2
            while ((step == 2 and self.height < next_floor.height) or
                   step == - 2 and self.height > next_floor.height):
                self.height += step
                canvas.fill(WHITE)
                self.draw(canvas, lift_pic)
                building.draw(canvas)
                window.blit(canvas, (0, 0))
                pygame.display.update()
            self.call_time -= abs(next_floor.level - self.current_floor) / 2 + 2
                # pygame.time.delay(20)
                # self.draw(canvas, lift_pic)
                # pygame.display.update()
        # y = canvas.get_height() - MARGIN - (self.current_floor * FLOOR_HEIGHT)
        # self.upcoming.append(dest)
        # while self.upcoming:
        #     next_floor = self.upcoming.pop(0)
        #     self.height += 2
        #     self.draw(canvas, lift_pic, self.height)'''

# if self.upcoming:
        #     next_floor = self.upcoming.pop(0)
        #     step = -4 if next_floor > self.current_floor else 4
        #     while ((step == 4 and y < canvas.get_height() - MARGIN + FLOOR_HEIGHT // 2 ) or
        #     step == - 4 and y > canvas.get_height() - MARGIN + FLOOR_HEIGHT // 2 ):
        #         y += step



