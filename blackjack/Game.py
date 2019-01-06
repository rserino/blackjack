from Deck import Deck
from Hand import Hand

class Game(object):
  def __init__(self):
    self.deck = Deck()
    self.hands = [self.deck.deal(), self.deck.deal()]
    self.player = self.hands[0]
    self.dealer = self.hands[1]

  def start(self):
    again = True
    hit_stay_response = 'h'

    while again:
      if hit_stay_response.lower() == 'h':
        print("\nDealer hand:")
        self.dealer.print_dealer_hand()
        dealer_score = self.dealer.get_score()
      else:
        print("\nDealer hand:")
        self.dealer.print_hand()
        dealer_score = self.dealer.get_score()

      print("\n\nPlayer hand:")
      self.player.print_hand()
      player_score = self.player.get_score()
      print(f"Your score is {player_score}")

      if player_score == 21:
        if len(self.player.get_hand()) == 2:
          print("\nBlackjack!")
          again = False

        if len(self.player.get_hand()) > 2:
          if dealer_score < 18:
            print("\n21! Dealer turn.")
            self.dealer_turn(dealer_score, player_score)
            again = False

          if dealer_score > 18 and dealer_score <= 21:
            player_win = 3
            again = False

      if player_score < 21:
        print("\nWould you like to hit or stay?")
        hit_stay_response = Game.get_validated_input(
          "h/s > ",
          ['h', 's']
        )

      if hit_stay_response.lower() == 'h':
        self.player.append_hit(self.deck.hit())
      else:
        print('\nStayed.')
        print("\nDealer hand:")
        self.dealer.print_hand()
        dealer_score = self.dealer.get_score()
        print(f"Dealer score is {dealer_score}")
        player_win = self.dealer_turn(dealer_score, player_score)
        again = False

      if player_score > 21:
        print("\nBust!")
        player_win = 2
        again = False

  def dealer_turn(self, dealer_score, player_score):
    if dealer_score < 17 and dealer_score <= player_score:
      print("\nDealer hits.")
      self.dealer.append_hit(self.deck.hit())
      print("\nDealer hand:")
      self.dealer.print_hand()
      dealer_score = print(f"Dealer score is {self.dealer.get_score()}")
      self.dealer_turn(self.dealer.get_score(), player_score)
    else:
      Game.evaluate_result(dealer_score, player_score)

  def evaluate_result(dealer_score, player_score):
    if dealer_score > 21:
      print("\nDealer Bust! You win!\n")
    else:
      if dealer_score > player_score:
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
