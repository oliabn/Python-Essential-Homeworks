"""
Опишіть класи графічного об'єкта, прямокутника та об'єкта, який
може обробляти натискання миші. Опишіть клас кнопки.
Створіть об'єкт кнопки та звичайного прямокутника.
Викличте метод натискання на кнопку.
"""

import pygame

pygame.init()


class Rectangle:
    """
    Draw rectangle
    param:
    rgb = (R, G, B), 0-255
    x_coord, y_coord, where 0 in upper left corner of the window
    width, height
    """

    def __init__(self, rgb, x, y, width, height):
        self.rgb = rgb
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window: pygame.Surface):
        size = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.rgb, size)
        pygame.display.flip()


class PressMouse:
    """
    Returns True if the mouse button is pressed
    (For Executes the right-click event.)
    """

    @staticmethod
    def click_event():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return True


class Button(Rectangle, PressMouse):
    """
    Button
    param:
    rgb = (R, G, B), 0-255
    x - x_coord, y - y_coord,
    button width, button height,
    name - text on the button
    """

    def __init__(self, rgb, x, y, width, height, name):
        super().__init__(rgb, x, y, width, height)
        self.name = name
        self.change_color = True  # for click_button_event

    def draw(self, window, new_rgb=None):
        # draw rectangle
        new_rgb = self.rgb if not new_rgb else new_rgb
        size = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, new_rgb, size)

        # draw button name
        font = pygame.font.Font(None, self.height // 2)
        text_color = (self.rgb[0] + 100) % 255, (self.rgb[1] + 100) % 255, (self.rgb[2] + 100) % 255
        text = font.render(self.name, True, text_color)
        window.blit(text, (self.x + self.width/6, self.y + self.height/3))
        pygame.display.update()

    def _is_button_area(self):
        """Check whether we pressed on the rectangle area"""

        return (self.x <= pygame.mouse.get_pos()[0] <= (self.x + self.width)
                and self.y <= pygame.mouse.get_pos()[1] <= (self.y + self.height))

    def click_button_event(self):
        """Changes the button color when pressed on it"""

        if self.click_event():
            if self._is_button_area():
                self._change_button_color()

    def _change_button_color(self):
        if self.change_color:
            new_rgb = (self.rgb[0] + 10) % 255, (self.rgb[1] + 10) % 255, (self.rgb[2] + 10) % 255
            self.draw(window, new_rgb)
            self.change_color = False
        else:
            self.draw(window, self.rgb)
            self.change_color = True


# set program window
window = pygame.display.set_mode((300, 260))
pygame.display.set_caption("Press the Button")

# create and draw rect
rect = Rectangle((0, 150, 200), 70, 45, 150, 60)
rect.draw(window)

# create and draw button
button = Button((0, 100, 250), 70, 150, 150, 60, 'Press me')
button.draw(window)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        button.click_button_event()
