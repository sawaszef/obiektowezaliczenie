# okno główne
import pygame
import random


SIZESCREEN = WIDTH, HEIGHT = 800, 750
screen = pygame.display.set_mode(SIZESCREEN)
pygame.font.init()

# font
LETTERBOX_FONT = pygame.font.Font("FreeSansBold.otf", 50)
KEYBOARD_FONT = pygame.font.Font("FreeSansBold.otf", 25)
KEYBOARD_LAYOUT = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
ALPHABET = "QWERTYUIOPASDFGHJKLZXCVBNM"

# # grafika  - wczytywanie grafik
GAME_BACKGROUND = pygame.image.load("./images/Starting Tiles.png")
BG_COLOR = (18, 18, 19)
BG_YELLOW = (181, 159, 59)
BG_GREEN = (83, 141, 78)
BG_GRAY = (58, 58, 60)

LETTER_SIZE = 77

guesses = 0
