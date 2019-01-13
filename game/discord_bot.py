import discord

import os
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = discord.Client()
import classes

game = None

@client.event
async def on_message(message):
  global game

  if message.author == client.user:
    return

  if message.content.startswith('!blackjack'):
    response = f'It looks like {message.author} wants to play Blackjack!'
    await client.send_message(message.channel, response)
    game = classes.DiscordGame(str(message.author))
    

  if message.content.startswith('!hit') and ongoing_game and not hit_lock:
    await client.send_message(message.channel, hand + '; Your score is ' + str(score))


            
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)


# msg = '{0.author.mention} ♥♦♣♠ Welcome to Blackjack ♠♣♦♥'.format(message)