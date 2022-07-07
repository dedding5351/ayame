from enum import Enum

value_mapping = {
    'low_ace': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'jack': 10,
    'queen': 10,
    'high_ace': 11
}


class CardValue(Enum):
    TWO = 'two'
    THREE = 'three'
    FOUR = 'four'
    FIVE = 'five'
    SIX = 'six'
    SEVEN = 'seven'
    EIGHT = 'eight'
    NINE = 'nine'
    TEN = 'ten'
    JACK = 'jack'
    QUEEN = 'queen'
    KING = 'king'
    # Default aces to low ace
    LOW_ACE = 'low_ace'
    HIGH_ACE = 'high_ace'


class CardSuit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    DIAMONDS = 'diamonds'
    HEARTS = 'hearts'


class Card:
    
    value: CardValue
    suit: CardSuit

    def __init__(self, value: CardValue, suit: CardSuit):
        self.value = value
        self.suit = suit

    def get_numeric_value(self) -> int:
        return value_mapping[self.value]

    def to_string(self) -> str:
        return f"{self.get_numeric_value()} of {self.suit}"