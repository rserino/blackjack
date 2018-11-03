# Work with Python 3.6
import discord
import os
from dotenv import load_dotenv
load_dotenv()
client = discord.Client()
from Game import Game

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!blackjack'):
        msg = '{0.author.mention} ♥♦♣♠ Welcome to Blackjack ♠♣♦♥'.format(message)
        game = Game()
        
        await client.send_message(message.channel, msg)
        await client.send_message(message.channel, game.get_hands())

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)