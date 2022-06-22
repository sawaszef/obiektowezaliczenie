import letter as l


class Word:

    def __init__(self):
        self.letters = []
        self.letters_str = ""

    def add_letter(self, letter):
        self.letters.append(letter)
        self.letters_str += letter.text
        print(self.letters_str)

    def delete_letter(self, surface):
        self.letters[-1].delete(surface)
        self.letters.pop()
        self.letters_str = self.letters_str[:-1]
        print(self.letters_str)

    def clear(self):
        self.letters.clear()
        self.letters_str = ""
        print(self.letters_str)
        l.Letter.current_letter_pos[1] += l.Letter.LETTER_Y_SPACING
        l.Letter.current_letter_pos[0] = 190
