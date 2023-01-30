import unittest

from bowling_game import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_max_score(self):
        score_expected = 300
        self._roll_many(10, 12)
        self.assertEqual(score_expected, self.game.total_score())

    def test_min_game(self):
        score_expected = 0
        self._roll_many(0, 20)
        self.assertEqual(score_expected, self.game.total_score())

    def test_simple_game(self):
        score_expected = 59
        for pins in [6, 2, 2, 6, 2, 4, 3, 2, 1, 2, 1, 6, 3, 5, 1, 6, 0, 4, 0, 3]:
            self.game.roll(pins)
        self.assertEqual(score_expected, self.game.total_score())

    def test_only_ones(self):
        score_expected = 20
        self._roll_many(1, 20)
        self.assertEqual(score_expected, self.game.total_score())

    def test_one_spare(self):
        score_expected = 16
        self._roll_spare()
        self.game.roll(3)
        self._roll_many(0, 17)
        self.assertEqual(score_expected, self.game.total_score())

    def test_one_strike(self):
        score_expected = 24
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self._roll_many(0, 16)
        self.assertEqual(score_expected, self.game.total_score())

    def _roll_many(self, pins, num):
        for i in range(num):
            self.game.roll(pins)

    def _roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)
