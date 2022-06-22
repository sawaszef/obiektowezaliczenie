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
                        for key in k.Key.ALL_KEYS:
                            key.bg_color = gm.BG_GREEN if key.text == letter.text else key.bg_color
                    else:
                        letter.bg_color = gm.BG_YELLOW
                        for key in k.Key.ALL_KEYS:
                            key.bg_color = gm.BG_YELLOW if key.text == letter.text and key.bg_color != gm.BG_GREEN else key.bg_color
                    self.solution_dict[letter.text.lower()] -= 1
                else:
                    letter.bg_color = gm.BG_GRAY
                    for key in k.Key.ALL_KEYS:
                        key.bg_color = gm.BG_GRAY if key.text == letter.text else key.bg_color

                letter.draw(surface)
                for key in k.Key.ALL_KEYS:
                    key.draw(surface)

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


