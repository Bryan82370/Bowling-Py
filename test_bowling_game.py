import unittest

from bowling_game import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_max_score(self):
        self._roll_many(10, 12)
        self.assertEqual(300, self.game.total_score())

    def test_min_game(self):
        self._roll_many(0, 20)
        self.assertEqual(0, self.game.total_score())

    def test_simple_game(self):
        for pins in [6, 2, 2, 6, 2, 4, 3, 2, 1, 2, 1, 6, 3, 5, 1, 6, 0, 4, 0, 3]:
            self.game.roll(pins)
        self.assertEqual(59, self.game.total_score())

    def test_only_ones(self):
        self._roll_many(1, 20)
        self.assertEqual(20, self.game.total_score())

    def test_one_spare(self):
        self._roll_spare()
        self.game.roll(3)
        self._roll_many(0, 17)
        self.assertEqual(16, self.game.total_score())

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self._roll_many(0, 16)
        self.assertEqual(24, self.game.total_score())

    def _roll_many(self, pins, num):
        for i in range(num):
            self.game.roll(pins)

    def _roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)