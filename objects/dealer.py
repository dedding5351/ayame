from objects.card import Card, CardSuit, CardValue

class Dealer:

    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.status = 'In-Play'
        self.name = "Dealer"

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
    
    def hidden_card(self):
        hand = []
        hand.append(self.hand[0].to_string())
        hand.append('??')

        return hand

    def get_hand(self):
        hand = []
        for card in self.hand:
            hand.append(card.to_string())

        return hand

    def reset_hand(self):
        self.hand = []
        self.hand_value = 0
        self.status = 'In-Play'        