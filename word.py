import letterbox as l


class Word:

    def __init__(self):
        self.letters = []

    def add_letter(self, letter):
        self.letters.append(letter)

    def delete_letter(self, surface):
        self.letters[-1].delete(surface)
        self.letters.pop()

    def clear(self):
        self.letters.clear()
        l.Letter.current_letter_pos[1] += l.Letter.LETTER_Y_SPACING
        l.Letter.current_letter_pos[0] = 190
