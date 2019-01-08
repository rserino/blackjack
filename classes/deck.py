import random

import classes

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
        deck.append(classes.Card(value, suit))

    return deck

  def deal(self):
    random.shuffle(self.deck)

    card_one = self.deck.pop(0)
    card_two = self.deck.pop(0)

    return classes.Hand([card_one, card_two])

  def hit(self):
    return self.deck.pop(0)
  
  def pull_card(self, value, suit):
    card = [card for card in self.deck if card.value == value and card.suit == suit][0]
    return self.deck.pop(self.deck.index(card))
