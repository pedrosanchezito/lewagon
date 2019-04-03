import string
import random

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        temp_grid = self.grid

        if len(word) > 0 and len(word) <= len(temp_grid):
            for letter in word:
                if letter in temp_grid:
                    temp_grid.remove(letter)
                else:
                    return False
                return True
        return False

if __name__ == '__main__':
    GAME = Game()
