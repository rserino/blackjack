from Deck import Deck
from Hand import Hand

class Game(object):
  def __init__(self):
    self.deck = Deck()
    self.hands = [self.deck.deal(), self.deck.deal()]
    self.player = self.hands[0]
    self.dealer = self.hands[1]

  def run(self):
    self.player_turn()
    self.dealer_turn()
    
    self.print_hands()
    print(self.get_result())

  def player_turn(self):
    player_choice = True
    self.dealer.print_dealer_hand()

    while player_choice:
      print('You:', self.player.to_string(), '\n')

      if self.player.get_score() < 21:
        print("Would you like to hit or stay?")
        hit_stay_response = Game.get_validated_input(
          "h/s > ",
          ['h', 's']
        )

        if hit_stay_response.lower() == 'h':
          self.player.append_hit(self.deck.hit())
        else:
          player_choice = False
          print()
      elif self.player.get_score() == 21:
        if len(self.player.get_hand()) == 2:
          player_choice = False
        elif len(self.player.get_hand()) > 2:
          if self.dealer.get_score() < 18:
            player_choice = False
          elif self.dealer.get_score() > 18 and self.dealer.get_score() <= 21:
            player_choice = False
      else:
        player_choice = False

  def dealer_turn(self):
    player_score = self.player.get_score()
    dealer_score = self.dealer.get_score()

    if player_score >= 21 and len(self.player.get_hand()) > 2:
      return

    if dealer_score < 17 and dealer_score <= player_score:
      self.dealer.append_hit(self.deck.hit())
      self.dealer_turn()

  def get_result(self):
    player_score = self.player.get_score()
    dealer_score = self.dealer.get_score()

    if player_score == 21 and len(self.player.get_hand()) == 2:
      return 'You win!'
    elif dealer_score > 21:
      return 'Dealer Bust! You win!'
    else:
      if dealer_score > player_score or player_score > 21:
        return 'You lose!'
      elif dealer_score < player_score:
        return 'You win!'
      else:
        return 'Push!'

  def get_validated_input(message, responses):
    while True:
      response = input(message)
      if response in responses:
        return response

  def print_hands(self):
    print('Dealer:', self.dealer.to_string())
    print('You:', self.player.to_string(), '\n')
