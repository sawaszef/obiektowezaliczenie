import pygame
import os
import game_module as gm
import letter as l
import word as w
import validation as valid
import keyboard as k

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

# ustawienia ekranu gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
pygame.font.init()
clock = pygame.time.Clock()
screen.fill(gm.BG_COLOR)
pygame.display.set_caption("ŁORDL")

# Stworzenie słowa odgadywanego i walidatora odpowiedzi
current_guess = w.Word()
validator = valid.Validator()

# wgranie tła i klawiatury
screen.blit(gm.GAME_BACKGROUND, (188.5, 20))
k.Key.create_keyboard(screen)

# pętla główna gry
window_open = True
has_won = False
while window_open:

    if validator.guesses == 6:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
            elif event.key == pygame.K_RETURN:
                if len(current_guess.letters) == 5:
                    has_won, is_in_wordlist = validator.check_guess(current_guess, screen)
                    if is_in_wordlist:
                        current_guess.clear()
                        if has_won:
                            window_open = False

            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess.letters) > 0:
                    current_guess.delete_letter(screen)
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in gm.ALPHABET and key_pressed != "":
                    if len(current_guess.letters) < 5:
                        new_letter = l.Letter(key_pressed)
                        new_letter.draw(screen)
                        current_guess.add_letter(new_letter)

    pygame.display.flip()
    clock.tick(30)

if has_won:
    print("Wygrales!")
else:
    print(f"Przegrales, poprawne slowo to {validator.solution}")

pygame.quit()
