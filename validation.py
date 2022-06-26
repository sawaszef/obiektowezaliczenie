import random
import game_module as gm
import keyboard as k


class Validator:
    def __init__(self):
        self.words = []
        self.solution = ""
        self.solution_dict = {}
        self.guesses = 0
        self.pick_solution()

    def pick_solution(self):
        with open("wordlist.txt", 'r') as file:
            self.words = [word.rstrip("\n") for word in file.readlines()]
        self.solution = random.choice(self.words)
        self.solution_dict = {letter: self.solution.count(letter) for letter in self.solution}

    def check_guess(self, guess, surface):
        guess_str = ""
        if guess.letters_str.lower() in self.words:
            in_wordlist = True
            for index, letter in enumerate(guess.letters):
                guess_str += letter.text.lower()
                if letter.text.lower() in self.solution_dict.keys() and self.solution_dict[letter.text.lower()] > 0:
                    if self.solution[index] == letter.text.lower():
                        letter.bg_color = gm.BG_GREEN
                        k.Key.ALL_KEYS[letter.text].bg_color = gm.BG_GREEN
                        k.Key.ALL_KEYS[letter.text].fill = True
                        self.solution_dict[letter.text.lower()] -= 1
                    else:
                        letter.bg_color = gm.BG_YELLOW
                        if not k.Key.ALL_KEYS[letter.text].fill:
                            k.Key.ALL_KEYS[letter.text].bg_color = gm.BG_YELLOW
                            k.Key.ALL_KEYS[letter.text].fill = True
                        self.solution_dict[letter.text.lower()] -= 1
                else:
                    if not k.Key.ALL_KEYS[letter.text].fill:
                        k.Key.ALL_KEYS[letter.text].bg_color = gm.BG_GRAY
                    letter.bg_color = gm.BG_GRAY
                letter.draw(surface)
                k.Key.ALL_KEYS[letter.text].draw(surface)

            self.guesses += 1
            if guess_str == self.solution:
                has_won = True
            else:
                has_won = False
        else:
            in_wordlist = False
            has_won = False
        self.solution_dict = {letter: self.solution.count(letter) for letter in self.solution}
        return has_won, in_wordlist
