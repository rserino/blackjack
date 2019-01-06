import unittest
from blackjack.Hand import Hand
from blackjack.Card import Card

class TestHand(unittest.TestCase):
  def test_vanilla(self):
    '''Vanilla case'''
    hand = Hand([Card(5, '♥'), Card('A', '♥')])
    self.assertEqual(hand.get_score(), 16)

  def test_pair_aces(self):
    '''Pair aces'''
    hand = Hand([Card('A', '♥'), Card('A', '♦')])
    self.assertEqual(hand.get_score(), 12)

  def test_many_aces(self):
    '''Three aces and a five'''
    hand = Hand([Card(5, '♥'), Card('A', '♥'), Card('K', '♥'), Card('A', '♦'), Card('A', '♣')])
    self.assertEqual(hand.get_score(), 18)

  def test_weird_hand(self):
    '''Collapses previous single ace'''
    hand = Hand([Card(3, '♥'), Card('A', '♦'), Card(10, '♠'), Card(4, '♣'),])
    self.assertEqual(hand.get_score(), 18)

if __name__ == '__main__':
  unittest.main()