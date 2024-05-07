import random

values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
          '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Deck:
    def __init__(self, deck):
        self.deck = deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(0)


class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = []
        self.total = 0

    def place_bet(self, bet_amount):
        self.money -= bet_amount

    def add_card(self, new_card):
        self.hand.append(new_card)
        self.total += values[new_card[0:-1]]

    def add_winnings(self, winning_amount):
        self.money += winning_amount


class Dealer:
    def __init__(self):
        self.hand = []
        self.total = 0

    def add_card(self, new_card):
        self.hand.append(new_card)
        self.total += values[new_card[0:-1]]


