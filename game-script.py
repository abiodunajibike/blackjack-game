import random


class BlackJack(object):
    '''
    A basic interactive Blackjack game between a player and a dealer
    '''
    def __init__(self):
        # deck of 52 cards
        self.deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K'] * 4
        self.player_hand = []
        self.dealer_hand = []

    def get_user_input(self, prompt):
        '''
        Display prompt message and return user input
        '''
        return input(prompt).lower()

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

        print (f'Your hand contains {self.player_hand} with a total of '
               f'{player_hand_total}')

        print(f'Dealer"s face up card is {self.dealer_hand[0]}')

        if player_hand_total == 21:
            print('Congratulations! You are the winner courtesy of your natural blackjack')

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

        self.evaluate_initial_hand_total()


if __name__ == "__main__":
    blackjack = BlackJack()
    blackjack.play_game()
            
