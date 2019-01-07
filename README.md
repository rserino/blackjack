# blackjack
[![Build Status](https://travis-ci.org/rserino/blackjack.svg?branch=master)](https://travis-ci.org/rserino/blackjack)
## Setup
Create a `.env` file in the project's root directory and set
```
DISCORD_BOT_SECRET= . . .
```
inside the `.env` file accordingly.

Install dependencies by issuing the command
```
pip install -r requirements.txt
```

## Run
From the root project directory:
* `python blackjack/DiscordBot.py` to run the Discord bot
* `python blackjack/blackjack.py` to run the blackjack app locally
* `python -m unittest` to run unit tests