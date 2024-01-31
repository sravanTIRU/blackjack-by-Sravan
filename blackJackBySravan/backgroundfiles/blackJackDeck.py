from backgroundfiles.ranksAndSuitsForBlackJack import ranks, suits
from backgroundfiles.blackJackCard import Cards
from random import shuffle


class Deck:
    """
    Represents a deck of playing cards.

    Attributes:
        deck (list): A list containing `Cards` objects representing the entire deck.

    Methods:
        __init__(): Initializes the deck by creating `Cards` objects for each rank and suit combination.
        show_card_at(position): Returns the `Cards` object at the specified position in the deck.
        show_all_cards(): Prints a formatted representation of all cards in the deck.
        shuffle_deck(): Shuffles the cards in the deck.
        pop_a_card(): Removes and returns the top card from the deck.
    """

    def __init__(self):
        self.deck = []
        for every_rank in ranks:
            for every_suit in suits:
                new_card = Cards(every_rank, every_suit)
                self.deck.append(new_card)

    def show_card_at(self, position):
        """
        Returns the `Cards` object at the specified position in the deck.

        Args:
            position (int): The position of the card in the deck (1-indexed).

        Returns:
            Cards: The `Cards` object at the specified position.
        """
        return self.deck[position - 1]

    def show_all_cards(self):
        """
        Prints a formatted representation of all cards in the deck.

        Returns:
            str: An empty string.
        """
        for card in self.deck:
            print(card)
        return ''

    def shuffle_deck(self):
        """Shuffles the cards in the deck."""
        shuffle(self.deck)

    def pop_a_card(self):
        """
        Removes and returns the top card from the deck.

        Returns:
            Cards: The top card from the deck.
        """
        return self.deck.pop()
