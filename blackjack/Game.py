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
    self.dealer_turn(self.dealer.get_score(), self.player.get_score())
    self.evaluate_result(self.dealer.get_score(), self.player.get_score())

  def player_turn(self):
    player_choice = True

    while player_choice:

      self.print_current_hands()

      if self.player.get_score() < 21: 
        print("\nWould you like to hit or stay?")
        hit_stay_response = Game.get_validated_input(
          "h/s > ",
          ['h', 's']
        )
        if hit_stay_response.lower() == 'h':
          self.player.append_hit(self.deck.hit())
        else:
          print("\nStayed")
          player_choice = False
      elif self.player.get_score() == 21:
        if len(self.player.get_hand()) == 2:
          print("\nBlackjack!")
          player_choice = False
        elif len(self.player.get_hand()) > 2:
          if self.dealer.get_score() < 18:
            print("\n21! Dealer turn.")
            player_choice = False
          elif self.dealer.get_score() > 18 and self.dealer.get_score() <= 21:
            player_choice = False
      else:
        print("\nBust!")
        player_choice = False

  def dealer_turn(self, dealer_score, player_score):
    if player_score >= 21 and len(self.player.get_hand()) > 2:
      return

    if dealer_score < 17 and dealer_score <= player_score:
      print("\nDealer hits.")
      self.dealer.append_hit(self.deck.hit())
      print("\nDealer hand:")
      self.dealer.print_hand()
      dealer_score = print(f"Dealer score is {self.dealer.get_score()}")
      self.dealer_turn(self.dealer.get_score(), player_score)

  def evaluate_result(self, dealer_score, player_score):
    self.dealer.print_hand()
    print(self.dealer.get_score())
    self.player.print_hand()
    print(self.player.get_score())
    if player_score == 21 and len(self.player.get_hand()) == 2:
      print("\nYou win!\n")
    elif dealer_score > 21:
      print("\nDealer Bust! You win!\n")
    else:
      if dealer_score > player_score or player_score > 21:
        print("\nYou lose!\n")
      elif dealer_score < player_score:
        print("\nYou win!\n")
      else:
        print("\nPush!\n")

  def get_validated_input(message, responses):
    while True:
      response = input(message)
      if response in responses:
        return response

  def print_current_hands(self):
    print("\nDealer hand:")
    self.dealer.print_dealer_hand()

    print("\n\nPlayer hand:")
    self.player.print_hand()
    print(f"Your score is {self.player.get_score()}")