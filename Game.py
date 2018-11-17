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

        while again:
            print("\nDealer hand:")
            self.dealer.print_hand()
            dealer_score = self.dealer.calc_score()

            print("\n\nPlayer hand:")
            self.player.print_hand()
            player_score = self.player.calc_score()

            if player_score == 21 and len(self.player.get_hand()) == 2:
                print("Blackjack!")
                player_win = True
                again = False

            if player_score == 21 and len(self.player.get_hand()) > 2 and dealer_score < 18:
                self.dealer_turn(dealer_score, player_score)
                again = False

            if player_score == 21 and len(self.player.get_hand()) > 2 and dealer_score > 18 and dealer_score < 21:
                # print("You win!")
                player_win = True
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
                    player_win = self.dealer_turn(dealer_score, player_score)
                    again = False

            if player_score > 21:
                print("\nBust!")
                player_win = False
                again = False

        if player_win == True:
            print("\nYou win!")
        if player_win == False:
            print("\nYou lose!")
        print("Bye!\n")

    def dealer_turn(self, dealer_score, player_score):
        player_win = False
        if dealer_score < 17 and dealer_score <= player_score:
            self.dealer.append_hit(self.deck.hit())
            print("\nDealer hand:")
            self.dealer.print_hand()
            self.dealer_turn(self.dealer.calc_score(), player_score)

        if dealer_score >=17 and dealer_score < player_score:
            player_win = True
            # print("\nYou win!")

        if dealer_score >= 17 and dealer_score < 21 and dealer_score > player_score:
            player_win = False
            # print("\nDealer wins!")

        if dealer_score == player_score:
            player_win = False
            print("\nPush!")

        if dealer_score < 21 and dealer_score > player_score:
            player_win = False
            # print("\nDealer wins!")

        if dealer_score > 21:
            print("\nDealer Bust!")
            player_win = True

        return player_win


    def get_validated_input(message, responses):
        while True:
            response = input(message)
            if response in responses:
                return response
