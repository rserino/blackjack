# Work with Python 3.6
import discord
import os
from dotenv import load_dotenv
load_dotenv()
client = discord.Client()
from Game import Game


ongoing_game = False
game = ''
hit_lock = False

@client.event
async def on_message(message):
    global ongoing_game
    global game
    global hit_lock
 
    if message.author == client.user:
        return
 
    if message.content.startswith('!blackjack'):
        ongoing_game = True
        msg = '{0.author.mention} ♥♦♣♠ Welcome to Blackjack ♠♣♦♥'.format(message)
        await client.send_message(message.channel, msg)

        game = Game()
        score = game.player.calc_score()
        hand = game.player.to_string()

        await client.send_message(message.channel, hand + '; Your score is ' + str(score))

    if message.content.startswith('!hit') and ongoing_game and not hit_lock:
        hit_lock = True
        game.player.append_hit(game.deck.hit())
        score = game.player.calc_score()
        hand = game.player.to_string()

        #TODO: cover case where player dealt 21
        if score > 21:
            await client.send_message(message.channel, hand + '; Your score is ' + str(score))
            await client.send_message(message.channel, '#r3kt')
            ongoing_game = False
        
        if score < 21:
            await client.send_message(message.channel, hand + '; Your score is ' + str(score))
            await client.send_message(message.channel, score)

        if score == 21:
            await client.send_message(message.channel,hand + '; Your score is ' + str(score))
            await client.send_message(message.channel, 'gg')
            ongoing_game = False
        
        hit_lock = False
            
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)