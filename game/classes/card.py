class Card(object):
    def __init__(self, value, suit):
      self.value = value
      self.suit = suit

    def get_card(self):
      return self.value, self.suit

    def to_string(self):
      return str(self.value) + self.suit + ' '
