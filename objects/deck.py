from objects.card import Card, CardSuit, CardValue
from collections import deque
from typing import Deque
import random

class Deck:
    cards: Deque[Card] = deque()

    def __init__(self):

        # Construct deck
        for suit in CardSuit:
            for value in CardValue:
                # Create card except for LOW/HIGH_ACE
                if value not in {CardValue.LOW_ACE, CardValue.HIGH_ACE}:
                    card = Card(value, suit)
                    self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
