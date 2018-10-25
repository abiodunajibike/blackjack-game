import unittest
from game_script import BlackJack


class TestBlackJackGame(unittest.TestCase):

    def setUp(self):
        self.game = BlackJack()

    def test_select_card(self):
        selected_card = self.game.select_card()
        self.assertIn(selected_card, self.game.deck)


if __name__ == '__main__':
    unittest.main()
