import random


class BlackJack(object):
    '''
    A basic interactive Blackjack game between a player and a dealer
    '''
    def __init__(self):
        # deck of 52 cards
        self.deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K'] * 4
        self.game_choices = {'h': 'Hit', 's': 'Stand', 'q': 'Quit'}
        self.blackjack_value = 21
        self.player_hand = []
        self.dealer_hand = []

    def shuffle_deck(self):
        '''
        Shuffle deck of cards
        '''
        random.shuffle(self.deck)

    def select_card(self):
        '''
        Select a card from the top of deck of cards
        '''
        return self.deck.pop()

    def deal_cards(self, hand, num_of_cards):
        '''
        Deal card(s)
        '''
        for i in range(num_of_cards):
            hand.append(self.select_card())

    def calculate_hand_total(self, hand):
        hand_total = 0
        for card in hand:
            if card in ['T', 'J', 'Q', 'K']:
                card = 10
            elif card == 'A':
                # prevent going bust if hand_total is greater than 11
                if hand_total > 11:
                    card = 1
                else:
                    card = 11

            hand_total += card
        return hand_total

    def evaluate_initial_hand_total(self):
        '''
        Evaluate player's initial hand total to see if it's exactly
        21 for a blackjack.
        '''
        player_hand_total = self.calculate_hand_total(self.player_hand)

        print(f'Your hand contains {self.player_hand} with a total of '
              f'{player_hand_total}')

        print(f'Dealer"s face up card is {self.dealer_hand[0]}')

        blackjack_value = 21
        if player_hand_total >= blackjack_value:
            if player_hand_total == blackjack_value:
                print('Congratulations! You have a blackjack. '
                      'You win.')
            elif player_hand_total > blackjack_value:
                print('Your hand total is greater than 21. You lose!')
            exit()

    def play_game(self):
        print(
            """
            --------------------------------------\n
            Welcome to BlackJack Interactive Game!\n
            --------------------------------------
            """
        )

        # shuffle deck of cards
        self.shuffle_deck()

        # deal cards to player
        self.deal_cards(self.player_hand, 2)

        # deal cards to dealer
        self.deal_cards(self.dealer_hand, 1)

        # evaluate initial cards to see if there is a winner
        self.evaluate_initial_hand_total()

        game_choice = None
        while game_choice != 'None':
            game_choice = input(
                'Type h to Hit, s to Stand or q '
                'to Quit and press Enter button: '
            ).lower()
            if game_choice == '':
                continue

            if game_choice in ['h', 's', 'q']:
                if game_choice == 'h':
                    print('Hit')
                elif game_choice == 's':
                    print('Stand')
                else:
                    print('Quit game')
                    exit()
            else:
                print(f'The entered value: {game_choice} '
                      'is not an acceptable value.')


if __name__ == "__main__":
    blackjack = BlackJack()
    blackjack.play_game()
