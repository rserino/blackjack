from Deck import Deck
from Hand import Hand

class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.hands = [self.deck.deal(), self.deck.deal()]
        self.player = self.hands[0]
        self.dealer = self.hands[1]

    def get_hands(self):
        to_return = ''
        for hand in self.hands:
            for card in hand.get_hand():
                suit, value = card.get_card()
                to_return += (str(value) + suit + ' ')

        return to_return


    def start(self):
        again = True

        while again:
            print("\nDealer hand:")
            self.dealer.print_hand()
            dealer_score = self.dealer.calc_score()

            print("\n\nPlayer hand:")
            self.player.print_hand()
            player_score = self.player.calc_score()

            if dealer_score == 21:
                print("\nDealer Blackjack! You Lose!")
                again = False

            if player_score == 21:
                print("Blackjack!")
                self.dealer_turn(dealer_score)
                again = False

            if player_score < 21:
                print("\nWould you like to hit or stay?")
                hit_stay_response = Game.get_validated_input(
                    "h/s > ",
                    ['h', 's']
                )

                if hit_stay_response.lower() == 'h':
                    self.player.append_hit(self.deck.hit())
                else:
                    print('\nStayed.')
                    self.dealer_turn(dealer_score)
                    again = False

            if player_score > 21:
                print("\nBust! You Lose!")
                again = False

        print("Bye!")

    def dealer_turn(self, dealer_score):
        if dealer_score < 21:
            self.dealer.append_hit(self.deck.hit())
            print("\nDealer hand:")
            self.dealer.print_hand()
            self.dealer_turn(self.dealer.calc_score())
        if dealer_score == 21:
            print("\nDealer Blackjack! You Lose!")
        if dealer_score > 21:
            print("\nDealer Bust! You win!")


    def get_validated_input(message, responses):
        while True:
            response = input(message)
            if response in responses:
                return response
