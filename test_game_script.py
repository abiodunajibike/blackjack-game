import unittest
from game_script import BlackJack


class TestBlackJackGame(unittest.TestCase):

    def setUp(self):
        self.game = BlackJack()

    def test_select_card(self):
        deck = self.game.deck.copy()
        selected_card = self.game.select_card()
        # assert the deck contains the selected card
        self.assertIn(selected_card, deck)
        # assert the selected card is the last card in the deck
        self.assertEqual(selected_card, deck[-1])

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
