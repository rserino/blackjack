import random

class Hand(object):
    def __init__(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def print_hand(self):
        for card in self.hand:
            card_suit, card_value = card.get_card()
            print("┌───────┐")
            print(f"| {card_value}     |")
            print("|       |")
            print(f"|   {card_suit}   |")
            print("|       |")
            print(f"|     {card_value} |")
            print("└───────┘")

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

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_card(self):
        return self.suit, self.value


def main():

    deck = Deck()
    hand = deck.deal()
    hand.print_hand()
    hand.calc_score()



main()
