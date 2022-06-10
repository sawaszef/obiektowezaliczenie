import pygame
import os
import game_module as gm

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
# ustawienia ekarnu gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
clock = pygame.time.Clock()

window_open = True
while window_open:
    screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
