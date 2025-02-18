from config import *

def draw_spacer(canvas, top_left, color):
    """
    Draws the spacer at the top of the floor

    :param canvas: The Pygame surface to draw on
    :param top_left: The coordinates for the top left corner of the spacer
    :param color: The colour the spacer will be drawn in
    """
    x, y = top_left
    rect = pygame.Rect(x, y, FLOOR_WIDTH, SPACER_HEIGHT)
    pygame.draw.rect(canvas, color, rect)

class Floor:
    """
    Represents a floor in the building
    """

    def __init__(self, level, canvas):
        """
        Initialises a Floor object with its level and position

        :param level: The floors level
        :param canvas: The Pygame surface to draw on
        """
        self.level = level
        self.button_colour = WHITE #The default colour for the button
        self.height = canvas.get_height() - (MARGIN + (self.level * FLOOR_HEIGHT))#The floors y coordinate
        self.center = HORIZ_CENTER, self.height + FLOOR_HEIGHT // 2#The center point of the floor - used for drawing the button and checking if the button was pressed
        self.timer_pos = MARGIN * 2, self.height + FLOOR_HEIGHT // 2 - TIMER_HEIGHT // 2#The position for drawing the timer
        self.has_called = False#Tells you if there is a lift on the way to this floor already
        self.at_floor = False#Tells you if there is a lift currently at this floor
        self.time = None#The time for the timer to count down to

    def draw(self, canvas, image, spacer_colour=BLACK):
        """
        Draws the floor in its correct position with a spacer on top,
        calls the function to draw a button in the middle,
        and if applicable - calls the function to draw the countdown timer.

        :param canvas: The surface that gets drawn on
        :param image: The image that gets drawn on the canvas
        :param spacer_colour: The colour that the spacer will be drawn in (Default colour is black).
        :return: The floor drawn on the canvas in its correct position.
        """
        canvas.blit(image, (MARGIN, self.height)) #
        draw_spacer(canvas, (MARGIN, self.height), spacer_colour)
        self.draw_button(canvas)
        if self.time:
            self.draw_timer(canvas)

    def draw_button(self, canvas):
        """
        Draws the call button with the floor number.

        :param canvas: The surface which gets drawn on
        """
        self.button_colour = GREEN if self.has_called else WHITE
        x, y = self.center
        horiz_num_move = - 9 if self.level > 9 else - 4  # determining the top left position to draw the numbers
        pygame.draw.circle(canvas, self.button_colour, (x, y), BUTTON_RADIUS) # Draw the button
        font = pygame.font.Font(None, 25) # Determine the font and size
        text = font.render(f'{self.level}', True, RED) # Determine the text and colour
        canvas.blit(text, (x + horiz_num_move, y + VERT_NUM_MOVE)) # Draw the text

    def is_calling(self, pos):
        """
        Determines if the floor is calling a lift

        :param pos: x, y coordinates of a mouse click
        :return: True if and only if the click was within the bounds of the button
        """
        cx, cy = pos
        x, y = self.center
        if ((cx - x) ** 2 + (cy - y) ** 2) ** 0.5 <= BUTTON_RADIUS: # Checks if the click was in the bounds of the button
            return True
        else:
            return False

    def draw_timer(self, canvas):
        """
        Draws the countdown timer if a lift is on the way.

        :param canvas: The surface which gets drawn on
        :return: A countdown timer drawn on the floor until a lift reaches the floor.
        """
        x, y = self.timer_pos # The coordinates for the timer's top left corner
        time_left = (self.time - pygame.time.get_ticks()) / 1000 # The time it shows
        if time_left >= 0: # Makes sure to only count down to zero
            pygame.draw.rect(canvas, BLACK, [x, y, TIMER_WIDTH, TIMER_HEIGHT]) # Draws the timer background
            font = pygame.font.Font(None, 25) # Determine the font and size
            text = font.render(str(time_left), True, WHITE) # Determine the text and colour
            canvas.blit(text, (x + TEXT_MARGIN, y + TEXT_MARGIN)) # Draw the time
        else:
            self.time = None # Stops drawing the timer





