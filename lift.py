from config import *

class Lift:

    def __init__(self, lift_id):
        self.id = lift_id
        self.current_floor = 0
        self.call_time = 0

    def draw(self, canvas, image):
        pass


    def __str__(self):
        return f'num: {self.id}'

    # def __get_call_time(self, dest):
    #     self.call_time += abs(dest - self.current_floor) / 2 + 2

    def draw_lift(self):
        canvas.blit(lift_pic, (self.window_width / 2 + 15 + (self.id * 90), self.window_height - 82))

# def draw_lifts(number):
#     for i in range(number):
#         canvas.blit(lift_pic, (width / 2 + 90 +(i * 75), height - 67))

def initialise_lifts(amount):
    lift_array =[]
    for i in range(1, amount + 1):
        lift_array.append(Lift(i))
    for lift in lift_array:
        lift.draw_lift()