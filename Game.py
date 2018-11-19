from Deck import Deck
from Hand import Hand


class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.hands = [self.deck.deal(), self.deck.deal()]
        self.player = self.hands[0]
        self.dealer = self.hands[1]

    def start(self):
        again = True
        player_win = 0
        hit_stay_response = 'h'

        while again:
            if hit_stay_response.lower() == 'h':
                print("\nDealer hand:")
                self.dealer.print_dealer_hand()
                dealer_score = self.dealer.calc_score()
            else:
                print("\nDealer hand:")
                self.dealer.print_hand()
                dealer_score = self.dealer.calc_score()

            print("\n\nPlayer hand:")
            self.player.print_hand()
            player_score = self.player.print_score()

            if player_score == 21 and len(self.player.get_hand()) == 2:
                print("Blackjack!")
                player_win = 1
                again = False

            if player_score == 21 and len(self.player.get_hand()) > 2 and dealer_score < 18:
                print("21! Dealers turn.")
                player_win = self.dealer_turn(dealer_score, player_score)
                again = False

            if player_score == 21 and len(self.player.get_hand()) > 2 and dealer_score > 18 and dealer_score < 21:
                player_win = 1
                again = False

            if player_score < 21:
                print("\nWould you like to hit or stay?")
                hit_stay_response = Game.get_validated_input(
                    "h/s > ",
                    ['h', 's']
                )

                if hit_stay_response.lower() == 'h':
                    self.player.append_hit(self.deck.hit())
                else:
                    print('\nStayed.')
                    print("\nDealer hand:")
                    self.dealer.print_hand()
                    dealer_score = self.dealer.print_score()
                    player_win = self.dealer_turn(dealer_score, player_score)
                    again = False

            if player_score > 21:
                print("\nBust!")
                player_win = 2
                again = False

        if player_win == 1:
            print("\nYou win!")
        if player_win == 2:
            print("\nYou lose!")
        if player_win == 3:
            print("\nPush!")
        print("Bye!\n")

    def dealer_turn(self, dealer_score, player_score):
        player_win = 0
        if dealer_score < 17 and dealer_score <= player_score:
            print("\nDealer Hits.")
            self.dealer.append_hit(self.deck.hit())
            print("\nDealer hand:")
            self.dealer.print_hand()
            return self.dealer_turn(self.dealer.print_score(), player_score)

        if dealer_score >=17 and dealer_score < player_score:
            player_win = 1
            return player_win

        if dealer_score >= 17 and dealer_score < 21 and dealer_score > player_score:
            player_win = 2
            return player_win

        if dealer_score == player_score:
            player_win = 3
            return player_win

        if dealer_score < 21 and dealer_score > player_score:
            player_win = 2
            return player_win

        if dealer_score > 21:
            print("\nDealer Bust!")
            player_win = 1
            return player_win

        if dealer_score == 21 and dealer_score > player_score:
            player_win = 2
            return player_win

        return player_win


    def get_validated_input(message, responses):
        while True:
            response = input(message)
            if response in responses:
                return response
