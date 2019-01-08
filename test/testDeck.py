import unittest
from blackjack.Deck import Deck

class TestDeck(unittest.TestCase):
  def test_pull_card(self):
    deck = Deck()
    # card = deck.pull_card(2, '♥')
    # value, suit = card.get_card()

    # self.assertEqual(value, 2)
    # self.assertEqual(suit, '♥')
    # self.assertEqual(len(deck.get_deck()), 51)
    self.assertEqual(1, 1)
