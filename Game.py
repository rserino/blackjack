from Deck import Deck

class Game(object):
    def __init__(self):
        self.game = self.start_game()


    def start_game(self):
        deck = Deck()
        hand = deck.deal()
        hand.print_hand()
        score = hand.calc_score()
        Game.post_deal(score)



    def post_deal(score):
        if score == 21:
            while True:
                print("Blackjack! Would you like to play again?")
                again_response = input("(y/n) > ")
                if again_response in ['y', 'Y']:
                    game = Game()
                    return game
                elif again_response in ['n', 'N']:
                    print("Ok bye!")
                    exit()
                else:
                    ("You must enter either a 'Y' or an 'N'.")
        if score < 21:
            while True:
                print("Would you like to hit or stay?")
                hit_stay_response = input("h/s > ")
                if hit_stay_response in ['h', 'H']:
                    pass
                elif hit_stay_response in ['s', 'S']:
                    pass
                else:
                    print("You must enter either an 'H' or a 'S'.")



    # def print_card(self):
    #     for card in self:
    #         card_suit, card_value = card.get_card()
    #         print(card_value, card_suit, ' ', end = '', sep = '')