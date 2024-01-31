"""
In this Blackjack game, cards have suits ('Hearts', 'Diamonds', 'Spades', 'Clubs') and ranks
 ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace').
  The values dictionary maps each rank to its numeric value in the game.

Since it's a Blackjack game, the values of 'Jack', 'Queen', and 'King' are all considered as 10.
The 'Ace' can be valued as 11 or 1, depending on the sum of card values in the player's hand.
"""

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
