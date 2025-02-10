from call_button import *
#
# def initialise_buttons(floors):
#     buttons_list = []
#     for i in range(1, floors + 1):
#         buttons_list.append(CallButton(i))
#     return buttons_list
#
# def make_buttons(floors):
#     buttons_list = initialise_buttons(floors)
#     for button in buttons_list:
#         button.draw_button()
#
#
# print((make_buttons(num_of_floors)))

def initialise_buttons(floors):
    buttons_coords = []
    buttons_list = []
    for i in range(1, floors + 1):
        buttons_list.append(CallButton(i))
        buttons_coords.append(height + 37 - (i * 75))
    return buttons_list, buttons_coords

print((initialise_buttons(num_of_floors)[1]))