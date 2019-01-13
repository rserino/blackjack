import classes
import utils.db_connector as db

class DiscordGame(object):
  def __init__(self, initiator):
    print('Starting new game')
    DiscordGame.create_new_player(initiator)

  @staticmethod
  def create_new_player(player):
    if db.get_player_info(player):
      print('Player already exists in database')
    else:
      db.insert_player(player)