class Hand(object):
  def __init__(self, hand):
    self.hand = hand

  def get_hand(self):
    return self.hand

  def to_string(self):
    to_return = ''

    for card in self.hand:
      to_return += card.to_string()

    return to_return

  def append_hit(self, new_card):
    self.hand.append(new_card)

  def print_hand(self):
    for card in self.hand:
      value, suit = card.get_card()
      print(value, suit, ' ', end = '', sep = '')

  def print_dealer_hand(self):
    deal_hand = []

    for card in self.hand:
      value, suit = card.get_card()
      deal_hand.append(value)
      deal_hand.append(suit)

    print('░ ', deal_hand[2], deal_hand[3], sep = '')

  def get_score(self):
    total_value = 0

    for card in self.hand:
      value, suit = card.get_card()

      if value in ['J', 'Q', 'K']:
        value = 10
      if value == 'A' and total_value < 11:
        value = 11
      if value == 'A' and total_value >= 11:
        value = 1

      total_value += value

    return total_value
