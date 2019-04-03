import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_is_valid(self):
        new_game = Game()
        new_game.grid = ['O', 'Q', 'U', 'W', 'R', 'B', 'A', 'Z', 'E']
        word = 'Baroque'
        self.assertEqual(new_game.is_valid(word), True)
