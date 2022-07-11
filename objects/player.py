from objects.card import Card, CardSuit, CardValue

class Player:

    def __init__(self, name, balance):
        self.hand = []
        self.hand_value = 0
        self.bet = 0
        self.status = 'In-Play'
        self.name = name
        self.balance = balance

    def get_hand_value(self, hand):
        total = 0

        for card in hand:
            if card.value.value == 'ace' and total + 11 > 21:
                total += 1
                continue
            elif card.value.value == 'ace':
                total += 11
                continue

            total += card.get_numeric_value()       
        self.hand_value = total

    def get_hand(self):
        hand = []
        for card in self.hand:
            hand.append(card.to_string())

        return hand

    def reset_hand(self):
        self.hand = []
        self.hand_value = 0
        self.status = 'In-Play'

    def main_bet(self, bet):
        self.bet = bet
        self.balance = self.balance - bet
    
    def hand_won(self):
        self.balance += self.bet*2
        self.bet = 0

    def hand_blackJack(self):
        self.balance += self.bet*(3/2)
        self.bet = 0

    def hand_push(self):
        self.balance += self.bet
        self.bet = 0

    def hand_lose(self):
        self.bet = 0