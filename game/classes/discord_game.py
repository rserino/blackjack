import classes
import utils.db_connector as db

class DiscordGame(object):
  def __init__(self, initiator):
    print('Starting new game')
    DiscordGame.create_new_player(initiator)
    
    self.deck = classes.Deck()
    self.hands = [self.deck.deal(), self.deck.deal()]
    self.player = self.hands[0]
    self.dealer = self.hands[1]

    self.terminal = self.player.get_score() == 21
    self.status =  f'Your hand: {self.player.to_string()}\nDealer hand: {self.dealer.dealer_hand_to_string()}\n'
    self.status += 'Blackjack!' if self.terminal else '`!hit` or `!stay`?'

  def player_hit(self):
    self.player.append_hit(self.deck.hit())

    if self.player.get_score() < 21:
      self.status = f'Your hand: {self.player.to_string()}'
    elif self.player.get_score() == 21:
        if len(self.player.get_hand()) == 2:
          self.terminal = True
          self.status = f'Your hand: {self.player.to_string()}\nYou win!'
        else:
          #dealer rebuttal
          pass
    else:
      self.terminal = True
      self.status = f'Your hand: {self.player.to_string()}\nYou lose!'

  def player_stay(self):
    pass

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

    self.status = f'Your hand: {self.player.to_string()}\nDealer hand: {self.dealer.to_string()}'

    if player_score == 21 and len(self.player.get_hand()) == 2:
      self.status += '\nYou win!'
    elif dealer_score > 21:
      self.status += '\nDealer Bust! You win!'
    else:
      if dealer_score > player_score or player_score > 21:
        self.status += '\nYou lose!'
      elif dealer_score < player_score:
        self.status += 'You win!'
      else:
        self.status += '\nPush!'
    return self.status

  @staticmethod
  def create_new_player(player):
    if db.get_player_info(player):
      print('Player already exists in database')
    else:
      db.insert_player(player)