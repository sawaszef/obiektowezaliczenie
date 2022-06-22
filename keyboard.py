import letterbox as lb
import pygame
import game_module as gm


class Key(lb.Letterbox):

    ALL_KEYS = []
    LETTER_X_SPACING = 40
    LETTER_Y_SPACING = 35
    current_letter_pos = [190, 600]

    def __init__(self, text):
        super().__init__(text, Key.current_letter_pos[0], Key.current_letter_pos[1], 15, 15)
        self.bg_rect = (self.x, self.y, gm.KEYBOARD_LETTER_SIZE, gm.KEYBOARD_LETTER_SIZE)
        self.text_surface = gm.KEYBOARD_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)
        Key.ALL_KEYS.append(self)

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.bg_rect)
        if self.bg_color == gm.BG_COLOR:
            pygame.draw.rect(surface, gm.BG_GRAY, self.bg_rect, 3)
        self.text_surface = gm.KEYBOARD_FONT.render(self.text, True, self.text_color)
        surface.blit(self.text_surface, self.text_rect)
        Key.current_letter_pos[0] += Key.LETTER_X_SPACING


