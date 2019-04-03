import string
import random
import requests
import json

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):

        r = requests.get(f'https://wagon-dictionary.herokuapp.com/{word}')
        if r.json()['found']:
            temp_grid = self.grid
            for letter in word:
                if letter in temp_grid:
                    temp_grid.remove(letter)
                else:
                    return False
                return True
        return False

if __name__ == '__main__':
    GAME = Game()
