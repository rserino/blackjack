import requests
import json

DB_URI = 'http://api:5000/players'

def get_player_info(player):
  print('Querying for player', player)
  response = requests.get(DB_URI, params={ 'name': player })
  print('Response', response.text)
  try:
    return json.loads(response.text)
  except:
    return response.text

def insert_player(player):
  print('Inserting player', player)
  response = requests.post(DB_URI, json = { "name": player })
  print('Response', response.text)
  return json.loads(response.text)