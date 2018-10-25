import unittest
from game_script import BlackJack


class TestBlackJackGame(unittest.TestCase):

    def setUp(self):
        self.game = BlackJack()

    def test_select_card(self):
        selected_card = self.game.select_card()
        self.assertIn(selected_card, self.game.deck)

    def test_deal_card(self):
        hand = []
        # deal 1 card
        self.game.deal_card(hand, 1)
        self.assertEqual(len(hand), 1)
        self.assertEqual(len(self.game.deck), 51)
        # clear hand and deal 2 cards
        hand.clear()
        self.game.deal_card(hand, 2)
        self.assertEqual(len(hand), 2)
        self.assertEqual(len(self.game.deck), 49)


if __name__ == '__main__':
    unittest.main()
