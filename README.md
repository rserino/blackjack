# blackjack
[![Build Status](https://travis-ci.org/rserino/blackjack.svg?branch=develop)](https://travis-ci.org/rserino/blackjack)
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

## Run in console
From the `/game` directory:
* `python main.py` to run blackjack in the terminal
* `python -m unittest` to run unit tests

## Run with Docker
* `docker-compose build`
* `docker-compose up`