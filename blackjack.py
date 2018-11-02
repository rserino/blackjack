import random

# class Game():
#     def __init__(self, player, dealer, deck):
#         self.player = player
#         self.dealer = dealer
#         self.deck = deck
#
#     def create_deck(self):
#         deck = []
#         suits = ['♥', '♦', '♣', '♠']
#         values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
#
#         for suit in suits:
#             for value in values:
#                 deck.append(Card(suit, value))
#
#         return deck
#
# class Dealer():
#     def __init__(self, hand, score):
#         self.hand = hand
#         self.score = score

class Player():
    def __init__(self, hand, score):
        self.hand = hand
        self.score = score

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_card(self):
        return self.suit, self.value

def print_hand(hand):
    for cards in hand:
        card_suit = cards[0]
        card_value = cards[1]
        print("┌───────┐")
        print(f"| {card_value}     |")
        print("|       |")
        print(f"|   {card_suit}   |")
        print("|       |")
        print(f"|     {card_value} |")
        print("└───────┘")

def calc_score(hand):
    total_value = 0
    for cards in hand:
        card_value = cards[1]
        if card_value == 'J' or card_value == 'Q' or card_value == 'K':
            card_value = 10
        if card_value == 'A' and total_value < 11:
            card_value = 11
        if card_value == 'A' and total_value >= 11:
            card_value = 1
        total_value += card_value
    print(f"Your score is {total_value}")
    return total_value

def create_deck():
    deck = []
    suits = ['♥', '♦', '♣', '♠']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    for suit in suits:
        for value in values:
            deck.append(Card(suit, value))

    return deck

def deal(deck):
    random.shuffle(deck)

    card_one = Card.get_card(deck.pop(0))
    card_two = Card.get_card(deck.pop(0))

    current_hand = [card_one, card_two]
    print_hand(current_hand)
    player_score = calc_score(current_hand)

    player_one = Player(current_hand, player_score)

def main():
    deck = create_deck()
    deal(deck)

main()
