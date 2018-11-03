from Deck import Deck
from Hand import Hand

class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.hands = [self.deck.deal()]
        self.hand = self.hands[0]

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
            self.hand.print_hand()
            score = self.hand.calc_score()

            if score == 21:
                print("Blackjack!")
                again = False

            if score < 21:
                print("Would you like to hit or stay?")
                hit_stay_response = Game.get_validated_input(
                    "h/s > ",
                    ['h', 's']
                )

                if hit_stay_response.lower() == 'h':
                    self.hand.append_hit(self.deck.hit())
                else:
                    print('Stayed.')
                    again = False

            if score > 21:
                print("Bust! You Lose!")
                again = False

        print("Bye!")
    
    def get_validated_input(message, responses):
        while True:
            response = input(message)
            if response in responses:
                return response


