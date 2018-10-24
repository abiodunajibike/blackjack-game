import random


class BlackJack(object):
    '''
    A basic interactive Blackjack game between a player and a dealer
    '''
    def __init__(self):
        # deck of 52 cards
        self.deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K']*4
        self.player_hand = []
        self.dealer_hand = []

    def get_user_input(prompt):
        '''
        Display prompt message and return user input
        '''
        return input(prompt)

    def shuffle_deck(self):
        '''
        Shuffle deck of cards
        '''
        random.shuffle(self.deck)

    def select_card(self):
        '''
        Select a random card from deck of cards
        '''
        self.shuffle_deck()
        return random.choice(self.deck)
        
    def deal_cards(self, hand):
        '''
        Deal 2 cards to player/dealer
        '''
        for i in range(2):
            hand.append(self.select_card())

    def play_game(self):
        print(
            """
            --------------------------------------\n
            Welcome to BlackJack Interactive Game!\n
            --------------------------------------
            """
        )

        # deal cards to player
        self.deal_cards(self.player_hand)
        print(f'self.player_hand: {self.player_hand}')

        # deal cards to dealer
        self.deal_cards(self.dealer_hand)
        print(f'self.player_hand: {self.dealer_hand}')


if __name__ == "__main__":
    blackjack = BlackJack()
    blackjack.play_game()
            
