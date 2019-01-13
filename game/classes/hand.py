import itertools

class Hand(object):
  def __init__(self, hand):
    self.hand = hand

  def get_hand(self):
    return self.hand

  def append_hit(self, new_card):
    self.hand.append(new_card)

  def to_string(self):
    to_return = ''

    for card in self.hand:
      to_return += card.to_string()

    return to_return.rstrip() + '; ' + str(self.get_score())

  def dealer_hand_to_string(self):
    return f'░░ {self.hand[1].value}{self.hand[1].suit}'

  def print_dealer_hand(self):
    deal_hand = []

    for card in self.hand:
      value, suit = card.get_card()
      deal_hand.append(value)
      deal_hand.append(suit)

    print('Dealer: ░ ', deal_hand[2], deal_hand[3], sep = '')

  def get_score(self):
    non_aces = list(filter(lambda card : card.get_card()[0] != 'A', self.hand))
    num_aces = len(self.hand) - len(non_aces)
    total_score = sum([card.value if card.value not in ['J', 'Q', 'K'] else 10 for card in non_aces])

    best_score = total_score

    for combination in itertools.product(*[[1, 11] for i in range (num_aces)]):
      potential_score = sum(combination) + total_score

      if potential_score <= 21 and potential_score > best_score:
        best_score = potential_score

    return total_score + num_aces if best_score == total_score else best_score
