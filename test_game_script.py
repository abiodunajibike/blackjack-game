from unittest import main, mock, TestCase
from game_script import BlackJack


class TestBlackJackGame(TestCase):

    def setUp(self):
        self.game = BlackJack()

    def test_shuffle_deck(self):
        before_shuffle_deck = self.game.deck.copy()
        self.game.shuffle_deck()
        after_shuffle_deck = self.game.deck
        self.assertNotEqual(before_shuffle_deck, after_shuffle_deck)

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

    def test_player_wins_with_evaluate_initial_hand_total(self):
        self.game.player_hand = [8, 'J', 3]  # ==> 21
        self.game.dealer_hand = [9]
        with self.assertRaises(SystemExit):
            self.game.evaluate_initial_hand_total()
        self.assertTrue(self.game.win)

    def test_player_wins_with_evaluate_hand_totals(self):
        self.game.player_hand = [8, 'J']  # ==> 18
        self.game.dealer_hand = [7, 'Q']  # ==> 17
        with self.assertRaises(SystemExit):
            self.game.evaluate_hand_totals()
        self.assertTrue(self.game.win)

    def test_player_loses_with_evaluate_hand_totals(self):
        self.game.player_hand = [8, 'J']  # ==> 18
        self.game.dealer_hand = [2, 9, 'Q']  # ==> 21
        with self.assertRaises(SystemExit):
            self.game.evaluate_hand_totals()
        self.assertFalse(self.game.win)

    def test_stand(self):
        self.game.dealer_hand = [2, 4, 5]

        with self.assertRaises(SystemExit):
            self.game.stand()
        self.assertEqual(len(self.game.dealer_hand), 4)

    def test_hit(self):
        hand = []
        self.game.hit(hand)
        self.assertEqual(len(hand), 1)
        self.assertEqual(len(self.game.deck), 51)

    def test_is_user_input_valid_with_valid_input(self):
        self.assertTrue(
            self.game.is_user_input_valid(
                list(self.game.game_choices.keys())[0]
            )
        )

    def test_is_user_input_valid_with_invalid_input(self):
        self.assertFalse(
            self.game.is_user_input_valid(
                'd'
            )
        )

    @mock.patch('game_script.BlackJack.get_input', return_value='h')
    def test_play_game_with_hit(self, input):
        with self.assertRaises(SystemExit):
            self.game.play_game()

    @mock.patch('game_script.BlackJack.get_input', return_value='s')
    def test_play_game_with_stand(self, input):
        with self.assertRaises(SystemExit):
            self.game.play_game()

    @mock.patch('game_script.BlackJack.get_input', return_value='q')
    def test_play_game_with_quit(self, input):
        with self.assertRaises(SystemExit):
            self.game.play_game()


if __name__ == '__main__':
    main()
