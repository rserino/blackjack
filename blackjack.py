import random


class Hand(object):
    def __init__(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def append_hit(self, new_card):
        self.hand.append(new_card)

    def print_hand(self):
        print("\n")
        for card in self.hand:
            card_suit, card_value = card.get_card()
            print(card_value, card_suit, ' ', end = '', sep = '')

    def calc_score(self):
        total_value = 0
        for card in self.hand:
            card_suit, card_value = card.get_card()
            if card_value in ['J', 'Q', 'K']:
                card_value = 10
            if card_value == 'A' and total_value < 11:
                card_value = 11
            if card_value == 'A' and total_value >= 11:
                card_value = 1
            total_value += card_value
        print(f"Your score is {total_value}")
        return total_value


class Deck(object):
    def __init__(self):
        self.deck = self.create_deck()

    def get_deck(self):
        return self.deck

    def create_deck(self):
        deck = []
        suits = ['♥', '♦', '♣', '♠']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

        for suit in suits:
            for value in values:
                deck.append(Card(suit, value))
        return deck

    def deal(self):
        random.shuffle(self.deck)

        card_one = self.deck.pop(0)
        card_two = self.deck.pop(0)

        return Hand([card_one, card_two])

    def hit(self):
        new_card = self.deck.pop(0)
        return new_card

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_card(self):
        return self.suit, self.value

class Game(object):
    def __init__(self):
        self.game = self.start_game()


    def start_game(self):
        deck = Deck()
        hand = deck.deal()
        hand.print_hand()
        score = hand.calc_score()
        Game.post_deal(score)



    def post_deal(score):
        if score == 21:
            while True:
                print("Blackjack! Would you like to play again?")
                again_response = input("(y/n) > ")
                if again_response in ['y', 'Y']:
                    game = Game()
                    return game
                elif again_response in ['n', 'N']:
                    print("Ok bye!")
                    exit()
                else:
                    ("You must enter either a 'Y' or an 'N'.")
        if score < 21:
            while True:
                print("Would you like to hit or stay?")
                hit_stay_response = input("h/s > ")
                if hit_stay_response in ['h', 'H']:
                    pass
                elif hit_stay_response in ['s', 'S']:
                    pass
                else:
                    print("You must enter either an 'H' or a 'S'.")



    # def print_card(self):
    #     for card in self:
    #         card_suit, card_value = card.get_card()
    #         print(card_value, card_suit, ' ', end = '', sep = '')


def main():

    game = Game()
    # deck = Deck()
    # hand = deck.deal()
    # hand.print_hand()
    # hand.calc_score()
    # hand.append_hit(deck.hit())
    # hand.print_hand()
    # hand.calc_score()
    # print(len(deck.get_deck()))


main()
