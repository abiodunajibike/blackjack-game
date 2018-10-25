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

    def test_calculate_hand_total(self):
        hand = [2, 'J', 5]  # ==> [2, 10, 5]
        hand_total = self.game.calculate_hand_total(hand)
        self.assertEqual(hand_total, 17)

        hand = [4, 'K', 'A']  # ==> [4, 10, 1]
        hand_total = self.game.calculate_hand_total(hand)
        self.assertEqual(hand_total, 15)

        hand = [6, 'A', 2]  # ==> [6, 11, 2]
        hand_total = self.game.calculate_hand_total(hand)
        self.assertEqual(hand_total, 19)

    def test_evaluate_initial_hand_total(self):
        self.game.player_hand = [2, 'J', 5]
        self.game.dealer_hand = [9]
        self.game.evaluate_initial_hand_total()


if __name__ == '__main__':
    unittest.main()
