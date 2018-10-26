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

    def deal_card(self, hand, num_of_cards):
        '''
        Deal card(s) to player/dealer
        '''
        for i in range(num_of_cards):
            card = self.select_card()
            print(f'Dealer selects card {card} from deck')
            print(f'{len(self.deck)} cards remaining')
            hand.append(card)

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
        21 for a blackjack. No need to evaluate dealer's hand now as
        it only contains one card and the maximum card value is 11.
        '''
        player_hand_total = self.calculate_hand_total(self.player_hand)

        print(f'Your hand contains {self.player_hand} with a total of '
              f'{player_hand_total}')

        print(f'Dealer face up card is {self.dealer_hand[0]}')

        if player_hand_total >= self.blackjack_value:
            if player_hand_total == self.blackjack_value:
                print('Congratulations! You win. You have a blackjack.')
            elif player_hand_total > self.blackjack_value:
                print('You lose! Your hand total is greater than 21.')
            exit()

    def evaluate_hand_totals(self):
        '''
        Evaluate both player and dealer hand total to determine
        who the winner is.
        '''
        player_hand_total = self.calculate_hand_total(self.player_hand)
        dealer_hand_total = self.calculate_hand_total(self.dealer_hand)

        print(f'Your hand contains {self.player_hand} with a total of '
              f'{player_hand_total}')
        print(f'Dealer hand contains {self.dealer_hand} with a total of '
              f'{dealer_hand_total}')

        if player_hand_total == self.blackjack_value:
            print('You win! You have a blackjack.')
        elif player_hand_total > self.blackjack_value:
            print('You lose! Your hand total exceeds 21.')
        elif dealer_hand_total == self.blackjack_value:
            print('You lose! Dealer has a blackjack.')
        elif dealer_hand_total > self.blackjack_value:
            print('Your win! Dealer hand total exceeds 21')
        elif player_hand_total > dealer_hand_total:
            print(f'Your win! Your hand total ({player_hand_total}) '
                  f'is greater than that of the dealer ({dealer_hand_total})')
        elif dealer_hand_total > player_hand_total:
            print(f'Your lose! Your hand total ({player_hand_total}) '
                  f'is less than that of the dealer ({dealer_hand_total})')
        exit()

    def stand(self):
        dealer_hand_total = self.calculate_hand_total(self.dealer_hand)

        if dealer_hand_total <= 16:
            self.hit(self.dealer_hand)

        self.evaluate_hand_totals()

    def hit(self, hand):
        self.deal_card(hand, 1)

    def play_game(self):
        print(
            "--------------------------------------\n"
            "Welcome to BlackJack Interactive Game!\n"
            "--------------------------------------"
        )

        print('Total number of cards at the start of '
              f'game is {len(self.deck)}')

        # shuffle deck of cards
        self.shuffle_deck()

        # deal cards to player
        self.deal_card(self.player_hand, 2)

        # deal cards to dealer
        self.deal_card(self.dealer_hand, 1)

        # evaluate initial cards to see if there is a winner
        self.evaluate_initial_hand_total()

        game_choice = None
        while game_choice != 'None':
            print('--------------------------------------------------------------')
            game_choice = input(
                'Type h to Hit, s to Stand or q '
                'to Quit and press Enter button: '
            ).lower()

            if game_choice == '':
                continue

            if game_choice in list(self.game_choices.keys()):
                print(
                    f'You have chosen to {self.game_choices[game_choice]}\n'
                    '--------------------------------------'
                )

                if game_choice == 'h':
                    self.hit(self.player_hand)
                    player_total = self.calculate_hand_total(self.player_hand)
                    if player_total > 21:
                        print('You lose! Hand total exceeds 21.')
                        exit()

                    # dealer must hit on 16 and lower cards
                    while self.calculate_hand_total(self.dealer_hand) <= 16:
                        self.hit(self.dealer_hand)
                    self.evaluate_hand_totals()
                elif game_choice == 's':
                    # dealer must hit on 16 and lower cards
                    while self.calculate_hand_total(self.dealer_hand) <= 16:
                        self.hit(self.dealer_hand)
                    self.evaluate_hand_totals()
                else:
                    print('Quit game')
                    exit()
            else:
                print(f'The entered value: {game_choice} '
                      'is not a valid choice.')


if __name__ == "__main__":
    blackjack = BlackJack()
    blackjack.play_game()
