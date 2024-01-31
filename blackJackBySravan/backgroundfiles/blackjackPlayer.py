class Player:
    """
    A class representing a player in a Blackjack game.

    Attributes:
    - name (str): The player's name in uppercase.
    - player_deck (list): A list to store the player's cards.
    - balance (int): The player's current account balance.

    Class Attribute:
    - max_balance (int): The maximum allowed balance for any player.

    Methods:
    - __init__(self, name): Initializes a new player with the given name and sets the initial balance.
    - collect_card(self, card_drawn): Adds a card to the player's deck.
    - debit_amount(self, debit_amount): Decreases the player's balance by the specified amount.
    - credit_amount(self, credit_amount): Increases the player's balance by the specified amount.
    - check_hand(self): Returns a string indicating the hand value of the player's cards.
    - check_balance(self): Returns a string indicating the player's current account balance.
    """

    max_balance = 2000

    def __init__(self, name):
        """
        Initializes a new player with the given name and sets the initial balance to the maximum allowed balance.

        Parameters:
        - name (str): The player's name.
        """
        self.name = name.upper()
        self.player_deck = []
        self.balance = Player.max_balance

    def collect_card(self, card_drawn):
        """
        Adds a card to the player's deck.

        Parameters:
        - card_drawn: The card to be added to the player's deck.
        """
        self.player_deck.append(card_drawn)

    def debit_amount(self, debit_amount):
        """
        Decreases the player's balance by the specified amount.

        Parameters:
        - debit_amount (int): The amount to be deducted from the player's balance.
        """
        self.balance -= debit_amount

    def credit_amount(self, credit_amount):
        """
        Increases the player's balance by the specified amount.

        Parameters:
        - credit_amount (int): The amount to be added to the player's balance.
        """
        self.balance += credit_amount

    def show_hand_value(self):
        """
        Calculate and return a string indicating the hand value of the player's cards.

        This method considers the special case for 'Ace' cards, which can have a value of 11 or 1
        depending on the overall sum of card values in the player's hand.

        Returns:
        - int: An integer indicating the hand value.
        """
        value_count = 0

        for card in self.player_deck:
            if card.value == 11:
                if value_count <= 10:
                    value_count += card.value
                else:
                    value_count += 1
            else:
                value_count += card.value
        return value_count

    def check_balance(self):
        """
        Returns a string indicating the player's current account balance.

        Returns:
        - str: A string indicating the player's account balance.
        """
        return f'\nAccount balance: {self.balance}'
