import pygame
import letterbox as l


class Word:

    guesses = 0

    def __init__(self):
        self.letters = []

    def add_letter(self, letter):
        self.letters.append(letter)

    def delete_letter(self, surface):
        self.letters[-1].delete(surface)
        self.letters.pop()

