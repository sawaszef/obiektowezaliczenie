# okno główne
import pygame, os
SIZESCREEN = WIDTH, HEIGHT = 1280, 720


# kolory
DARKGREEN = pygame.color.THECOLORS['darkgreen']
LIGHTBLUE = pygame.color.THECOLORS['lightblue']


screen = pygame.display.set_mode(SIZESCREEN)

# # grafika  - wczytywanie grafik
# path = os.path.join(os.pardir, 'images')
# file_names = sorted(os.listdir(path))
#
# file_names.remove('background.png')
# BACKGROUND = pygame.image.load(os.path.join(path, 'background.png')).convert()
# for file_name in file_names:
#     image_name = file_name[:-4].upper()
#     globals()[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND)
#
# # grafika gracza
# PLAYER_WALK_LIST_R = [PLAYER_WALK1_R, PLAYER_WALK2_R, PLAYER_WALK3_R,
#                       PLAYER_WALK4_R, PLAYER_WALK5_R, PLAYER_WALK6_R, PLAYER_WALK7_R]
#
