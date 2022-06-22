import pygame
import game_module as gm
import letterbox as lb


class Letter(lb.Letterbox):

    LETTER_X_SPACING = 85
    LETTER_Y_SPACING = 100
    current_letter_pos = [190, 20]

    def __init__(self, text):
        super().__init__(text, Letter.current_letter_pos[0], Letter.current_letter_pos[1], 36, 36)
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
