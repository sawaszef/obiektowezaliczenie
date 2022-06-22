import game_module as gm
from abc import ABC, abstractmethod


class Letterbox:
    def __init__(self, text, x, y, text_x, text_y):
        self.bg_color = gm.BG_COLOR
        self.text_color = (255, 255, 255)
        self.x = x
        self.y = y
        self.bg_rect = (self.x, self.y, gm.LETTER_SIZE, gm.LETTER_SIZE)
        self.text = text
        self.text_position = (self.x + text_x, self.y + text_y)

    @abstractmethod
    def draw(self, surface):
        pass
