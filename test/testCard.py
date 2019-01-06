import unittest
from blackjack.Card import Card

class TestCard(unittest.TestCase):
  def setUp(self):
    self.card = Card(5, '♥')

  def test_get_card(self):
    '''get_card() returns correct tuple'''
    self.assertEqual(self.card.get_card(), (5, '♥'))

  def test_to_string(self):
    '''to_string() returns correct string'''
    self.assertEqual(self.card.to_string(), '5♥ ')

if __name__ == '__main__':
  unittest.main()