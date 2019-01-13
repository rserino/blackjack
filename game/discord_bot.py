import discord

import os
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = discord.Client()
import classes

games = {}

@client.event
async def on_message(message):
  global game
  player = str(message.author)

  if message.author == client.user:
    return

  if message.content.startswith('!blackjack'):
    if player not in games:
      games[player] = classes.DiscordGame(player)

      await client.send_message(
        message.channel,
        f'Dealing in `{player}`\n{games[player].status}'
      )
    else:
      await client.send_message(message.channel, f'Game in progress for `{player}`')

  if message.content.startswith('!hit'):
    if player not in games:
      await client.send_message(message.channel, f'No game in progress for `{player}`')
    else:
      games[player].player_hit()
      await client.send_message(message.channel, games[player].status)
      if games[player].terminal:
        games.pop(player, None)

  if message.content.startswith('!stay'):
    if player not in games:
      await client.send_message(message.channel, f'No game in progress for `{player}`')
    else:
      games[player].dealer_turn()
      await client.send_message(message.channel, games[player].get_result())
      games.pop(player, None)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)


# msg = '{0.author.mention} ♥♦♣♠ Welcome to Blackjack ♠♣♦♥'.format(message)