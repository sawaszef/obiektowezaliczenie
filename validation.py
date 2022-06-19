import random
import game_module as gm


class Validator:
    def __init__(self):
        self.solution = "rifle"
        self.guesses = 0

    @staticmethod
    def pick_solution():
        with open("wordlist.txt", 'r') as file:
            words = [word.rstrip("\n") for word in file.readlines()]
        solution = random.choice(words)
        return solution

    def check_guess(self, guess, surface):
        guess_str = ""

        for index, letter in enumerate(guess.letters):
            guess_str += letter.text.lower()
            if letter.text.lower() in self.solution:
                if self.solution[index] == letter.text.lower():
                    letter.bg_color = gm.BG_GREEN
                else:
                    letter.bg_color = gm.BG_YELLOW
            else:
                letter.bg_color = gm.BG_GRAY
            letter.draw(surface)
        self.guesses += 1
        if guess_str == self.solution:
            return True
        return False
