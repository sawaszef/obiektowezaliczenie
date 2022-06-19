import pygame
import game_module as gm

class Letter:

    LETTER_X_SPACING = 85
    LETTER_Y_SPACING = 12
    current_letter_pos = [190, 20]

    def __init__(self, text):
        self.bg_color = gm.BG_COLOR
        self.text_color = (255, 255, 255)
        self.x = Letter.current_letter_pos[0]
        self.y = Letter.current_letter_pos[1]
        self.bg_rect = (self.x, self.y, gm.LETTER_SIZE, gm.LETTER_SIZE)
        self.text = text
        self.text_position = (self.x+36, self.y+36)
        self.text_surface = gm.LETTERBOX_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.bg_rect)
        if self.bg_color == gm.BG_COLOR:
            pygame.draw.rect(surface, gm.BG_GRAY, self.bg_rect, 3)
        self.text_surface = gm.LETTERBOX_FONT.render(self.text, True, self.text_color)
        surface.blit(self.text_surface, self.text_rect)
        Letter.current_letter_pos[0] += Letter.LETTER_X_SPACING

    def delete(self, surface):
        pygame.draw.rect(surface, gm.BG_COLOR, self.bg_rect)
        pygame.draw.rect(surface, gm.BG_GRAY, self.bg_rect, 3)
        pygame.display.update()
        Letter.current_letter_pos[0] -= Letter.LETTER_X_SPACING



