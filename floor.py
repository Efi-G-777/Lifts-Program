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
        Initialises a Floor object

        :param level: The floors level
        :param canvas: The Pygame surface to draw on
        """
        self.level = level
        self.button_colour = WHITE
        self.height = canvas.get_height() - (MARGIN + (self.level * FLOOR_HEIGHT))
        self.center = HORIZ_CENTER, self.height + FLOOR_HEIGHT // 2
        self.timer_pos = MARGIN * 2, self.height + FLOOR_HEIGHT // 2 - TIMER_HEIGHT // 2
        self.has_called = False
        self.at_floor = False
        self.time = None

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
        # x = MARGIN
        # y = self.height
        canvas.blit(image, (MARGIN, self.height))
        draw_spacer(canvas, (MARGIN, self.height), spacer_colour)
        self.draw_button(canvas)
        if self.time:
            self.draw_timer(canvas)

    def draw_button(self, canvas):
        """
        Draws the button in its correct place in the middle of the floor
        with the floor number written on it.

        :param canvas: The surface which gets drawn on
        :return: The button drawn on the floor
        """
        self.button_colour = GREEN if self.has_called else WHITE
        x, y = self.center
        horiz_num_move = - 9 if self.level > 9 else - 4  # determining the top left position to draw the numbers
        pygame.draw.circle(canvas, self.button_colour, (x, y), BUTTON_RADIUS)
        font = pygame.font.Font(None, 25)
        text = font.render(f'{self.level}', True, RED)
        canvas.blit(text, (x + horiz_num_move, y + VERT_NUM_MOVE))

    def is_calling(self, pos):
        """
        determines if the floor is calling a lift
        :param pos: x, y coordinates of a mouse click
        :return: True if and only if the click was within the bounds of the button
        """
        cx, cy = pos
        x, y = self.center
        if ((cx - x) ** 2 + (cy - y) ** 2) ** 0.5 <= BUTTON_RADIUS:
            return True
        else:
            return False

    def draw_timer(self, canvas):
        """
        Draws the countdown timer on the floor.
        :param canvas: The surface which gets drawn on
        :return: A countdown timer drawn on the floor until a lift reaches the floor.
        """
        x, y = self.timer_pos
        time_left = (self.time - pygame.time.get_ticks()) / 1000
        if time_left >= 0:
            pygame.draw.rect(canvas, BLACK, [x, y, TIMER_WIDTH, TIMER_HEIGHT])
            font = pygame.font.Font(None, 25)
            text = font.render(str(time_left), True, WHITE)
            canvas.blit(text, (x + TEXT_MARGIN, y + TEXT_MARGIN))
        else:
            self.time = None





