"""Defines a Cards class for creating and displaying playing cards with specified ranks and suits."""

from backgroundfiles.ranksAndSuitsForBlackJack import values


class Cards:

    """
    Represents a playing card with specified rank and suit.

    Args:
    rank (str): The rank of the card (e.g., 'two', 'ace').
    suit (str): The suit of the card (e.g., 'hearts', 'spades').

    Attributes:
    rank (str): The capitalized rank of the card.
    suit (str): The capitalized suit of the card.
    value (int): The numerical value associated with the card's rank.

    Methods:
    __str__(): Returns a formatted string representing the current card, with uppercase text.

    Note:
    The `values` dictionary is expected to be imported from the 'suitAndRanks' module.
    """

    def __init__(self, rank: str, suit: str):
        self.rank = rank.capitalize()
        self.suit = suit.capitalize()
        self.value = values[rank.capitalize()]

    def __str__(self):
        return f'{values[self.rank.capitalize()]} of {self.suit}'.upper()
