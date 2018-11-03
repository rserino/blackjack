from Deck import Deck
from Hand import Hand

class Game(object):
    def __init__(self):
        self.game = self.start_game()


    def start_game(self):
        self.deck = Deck()
        self.hands = [self.deck.deal()]

        self.hand = self.deck.deal()
        self.hand.print_hand()
        score = self.hand.calc_score()
        self.post_deal(score)

    def get_hands(self):
        to_return = ''
        for hand in self.hands:
            for card in hand.get_hand():
                suit, value = card.get_card()
                to_return += (str(value) + suit + ' ')

        return to_return


    def post_deal(score):
        if score == 21:
            while True:
                print("Blackjack! \nWould you like to play again?")
                again_response = input("(y/n) > ")
                if again_response in ['y', 'Y']:
                    game = Game()
                    return game
                elif again_response in ['n', 'N']:
                    print("Ok bye!\n")
                    exit()
                else:
                    ("You must enter either a 'Y' or an 'N'.")
        if score < 21:
            while True:
                print("Would you like to hit or stay?")
                hit_stay_response = input("h/s > ")
                if hit_stay_response in ['h', 'H']:
                    self.hand.append_hit(self.deck.hit())
                    self.hand.print_hand()
                    new_score = self.hand.calc_score()
                    self.post_deal(new_score)
                elif hit_stay_response in ['s', 'S']:
                    print("Chicken!\n""Would you like to play again?")
                    stay_response = input("(y/n) > ")
                    if stay_response in ['y', 'Y']:
                        game = Game()
                        return game
                    elif stay_response in ['n', 'N']:
                        print("Ok bye!")
                        exit()
                    else:
                        ("You must enter either a 'Y' or an 'N'.")
                else:
                    print("You must enter either an 'H' or a 'S'.")
        if score > 21:
            while True:
                print("Bust! You Lose! \nWould you like to play again?")
                again_response = input("(y/n) > ")
                if again_response in ['y', 'Y']:
                    game = Game()
                    return game
                elif again_response in ['n', 'N']:
                    print("Ok bye!")
                    exit()
                else:
                    ("You must enter either a 'Y' or an 'N'.")



    # def print_card(self):
    #     for card in self:
    #         card_suit, card_value = card.get_card()
    #         print(card_value, card_suit, ' ', end = '', sep = '')
