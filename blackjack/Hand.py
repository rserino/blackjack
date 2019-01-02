class Hand(object):
    def __init__(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def to_string(self):
        to_return = ''

        for card in self.hand:
            to_return += card.to_string()

        return to_return

    def append_hit(self, new_card):
        self.hand.append(new_card)

    def print_hand(self):
        # print("\n")
        for card in self.hand:
            card_suit, card_value = card.get_card()
            print(card_value, card_suit, ' ', end = '', sep = '')

    def print_dealer_hand(self):
        deal_hand = []
        for card in self.hand:
            card_suit, card_value = card.get_card()
            deal_hand.append(card_value)
            deal_hand.append(card_suit)
        print("░", ' ', deal_hand[2], deal_hand[3], sep = '')


    def calc_score(self):
        total_value = 0
        for card in self.hand:
            card_suit, card_value = card.get_card()
            if card_value in ['J', 'Q', 'K']:
                card_value = 10
            if card_value == 'A' and total_value < 11:
                card_value = 11
            if card_value == 'A' and total_value >= 11:
                card_value = 1
            total_value += card_value
        return total_value

    def print_score(self):
        total_value = 0
        for card in self.hand:
            card_suit, card_value = card.get_card()
            if card_value in ['J', 'Q', 'K']:
                card_value = 10
            if card_value == 'A' and total_value < 11:
                card_value = 11
            if card_value == 'A' and total_value >= 11:
                card_value = 1
            total_value += card_value
        print(f"Your score is {total_value}")

        return total_value