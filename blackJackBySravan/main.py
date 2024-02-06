"""
Strict Warning: Read Game Rules Before Playing!

This blackjack game implementation follows specific rules. It is strongly advised to read and understand the rules
before starting to play.

Failure to adhere to the rules may lead to unexpected outcomes and impact the gaming experience.

Game Rules:
- The objective is to beat the computer opponent by having a hand value closer to 21 without exceeding it.
- Each round involves placing a bet, receiving two cards, and making strategic decisions.
- The player wins by reaching a hand value of 21 or having a higher hand value than the computer without busting.
- The game continues until the player decides to quit or runs out of the minimum required balance (300).
- It is crucial to be familiar with commands (e.g., Hit, Stay) and betting rules before playing.

**!!!WARNING!!!: Do not use command input '6' unless you intend to exit the game.
 Using this command will immediately terminate the program.**

Refer to 'rules and logic' file for a detailed explanation of game rules and logic.

Follow the in-code comments for a better understanding of the game logic.

Good luck, and enjoy the game!
"""
import sys

# The rest of the code follows...


from backgroundfiles.blackjackPlayer import Player
from backgroundfiles.blackJackDeck import Deck

bets = 0


def switch_turn(current_turn):
    """
    Switches the turn between 'user' and 'computer'.

    Parameters:
    - current_turn (str): Current turn, either 'user' or 'computer'.

    Returns:
    - str: The new turn.
    """
    return 'user' if current_turn == 'computer' else 'computer'


def display_prompt():
    """
    Displays the command prompt for the user.
    """
    print('\n1. Show Hand'.upper())
    print('2. Check Balance'.upper())
    print('3. Hit'.upper())
    print('4. Stay'.upper())
    print('5. Show Bets'.upper())
    print('6. exit the program. !!!warning... terminates the program immediately.'.upper())


def take_input():
    """
    Takes user input for selecting a command.

    Returns:
    - int: The selected command as an integer.
    """
    player_choice = input('\nSelect a command: '.upper())
    while player_choice not in ['1', '2', '3', '4', '5', '6']:
        print('Invalid input. Please select a valid command.'.upper())
        player_choice = input('Select a command: '.upper())
    return int(player_choice)


def place_bet(p1: Player):
    """
    Places a bet for the player.

    Parameters:
    - p1 (Player): The player placing the bet.

    Returns:
    - int: The amount of the bet.
    """
    print('\nMaximum bet is 500.'.upper())

    while True:
        bet = input("Enter the number of 100's you want to place as a bet: ".upper())
        if bet.isdigit() and int(bet) in [1, 2, 3, 4, 5] and int(bet) * 100 <= p1.balance:
            break
        else:
            print("Invalid bet. Select from [1, 2, 3, 4, 5] and ensure it's within your balance.".upper())

    amount = int(bet) * 100
    p1.debit_amount(amount)
    return amount


def display_initial_cards(person: Player, bot: Player):
    """
    Displays the initial cards drawn for both players.

    Parameters:
    - user (Player): The user player.
    - computer (Player): The computer player.
    """
    print("\nInitial cards drawn:\n")
    print("User's cards:")
    for card in person.player_deck:
        print(card)
    print("\nComputer's cards:")
    print(bot.player_deck[0])  # Displaying the first card face up
    print("FACE DOWN")


def show_cards_in_hand(player: Player):
    """
    Displays the cards in the player's hand.

    Parameters:
    - player (Player): The player whose hand is to be displayed.
    """
    for card in player.player_deck:
        if card.value == 11:
            print(f'ACE OF {card.suit}'.upper())
        else:
            print(card)


def show_bets():
    """
    Displays the current total bets.
    """
    print('\nBETS:', bets)


def check_for_minimum_balance(player: Player):
    """
    Checks if the player's balance is above the minimum required balance.

    Parameters:
    - player (Player): The player to check.

    Returns:
    - bool: True if the balance is above the minimum, False otherwise.
    """
    return player.balance >= 300


def display_hand(player: Player):
    """
    Displays the cards in the player's hand and the hand value.

    Parameters:
    - player (Player): The player whose hand is to be displayed.
    """
    print()
    show_cards_in_hand(player)
    print(f'\n{player.name} HAND VALUE:', player.show_hand_value())


def check_for_win(p1: Player) -> bool:
    """
    Checks if the player has won by reaching a hand value of 21.

    Parameters:
    - p1 (Player): The player to check.

    Returns:
    - bool: True if the player has won, False otherwise.
    """
    return p1.show_hand_value() == 21


def check_for_higher_hand(primary: Player, secondary: Player):
    """
    Checks if the primary player has a higher hand value than the secondary player.

    Parameters:
    - primary (Player): The player with the potentially higher hand.
    - secondary (Player): The player with the potentially lower hand.

    Returns:
    - bool: True if the primary player has a higher hand value, False otherwise.
    """
    pr_value = primary.show_hand_value()
    sr_value = secondary.show_hand_value()
    return sr_value < pr_value < 22


def check_for_bust(p1: Player):
    """
    Checks if the player has busted (hand value greater than 21).

    Parameters:
    - p1 (Player): The player to check.

    Returns:
    - bool: True if the player has busted, False otherwise.
    """
    return p1.show_hand_value() > 21


if __name__ == '__main__':
    print("\nWelcome to 'Blackjack ROUNDS: Beat the Computer Opponent'!\n")

    user = Player('user')
    computer = Player('computer')

    game_deck = Deck()
    game_deck.shuffle_deck()

    round_number = 0

    while True:
        turn = 'user'
        round_number += 1

        print(f'\n-------- ROUND {round_number} -----------')
        print('Good luck! May the cards be in your favor!\n')

        print('REMAINING BALANCE:', user.balance)

        if not check_for_minimum_balance(user):
            print(user.check_balance())
            print('\nOut of minimum balance. Game over.'.upper())
            break

        bets += place_bet(user)

        if len(game_deck.deck) >= 3:
            for _ in range(2):
                user.player_deck.append(game_deck.pop_a_card())
                computer.player_deck.append(game_deck.pop_a_card())
            display_initial_cards(user, computer)
            print("computer hides it's second card!!!")
        else:
            print('\nCurrent deck has no more cards. Start a new game.'.upper())
            break

        while True:  # current game loop

            if check_for_win(user) or check_for_win(computer):
                uv = user.show_hand_value()
                cv = computer.show_hand_value()
                if uv > cv:
                    user.balance += bets * 1.5
                    bets = 0
                print('\nlucky draw.'.upper())
                print(f'\n{'user' if uv > cv else 'computer'} won the round'
                      f' with the starting hand equaling to 21.'.upper())
                break

            if turn == 'user':

                display_prompt()
                player_input = take_input()

                while True:

                    if player_input == 1:
                        display_hand(user)

                    elif player_input == 2:
                        print(user.check_balance())

                    elif player_input == 3:
                        user.player_deck.append(game_deck.pop_a_card())
                        display_hand(user)
                        if check_for_win(user):
                            user.balance += bets * 1.5
                            bets = 0
                            print('\nUser won the round!'.upper())
                            turn = 'user'
                            break
                        if check_for_bust(user):
                            print('\nYour hand value is more than 21. You are busted. Lost the round.'.upper())
                            turn = 'bust'
                            break

                    elif player_input == 4:
                        turn = switch_turn(turn)
                        break

                    elif player_input == 5:
                        show_bets()
                    elif player_input == 6:
                        sys.exit()  # !!! TERMINATES THE PROGRAM EXECUTION.

                    display_prompt()
                    player_input = take_input()

            elif turn == 'computer':

                while computer.show_hand_value() < 17:
                    computer.player_deck.append(game_deck.pop_a_card())

                display_hand(computer)

                if user.show_hand_value() == computer.show_hand_value():
                    user.balance += bets
                    bets = 0
                    print('\nThis round ended as a tie.'.upper())
                    break

                elif check_for_win(computer) or check_for_higher_hand(computer, user):
                    print('\nComputer won the round.'.upper())
                    turn = switch_turn(turn)
                    break

                elif check_for_bust(computer):
                    print('\nComputer hand value > 21. User won the round.'.upper())
                    turn = 'bust'
                    user.balance += bets * 1.5
                    break
                elif user.show_hand_value() > computer.show_hand_value():
                    print('\nUser hand value:'.upper(), user.show_hand_value())
                    print('User won the round with a higher hand value.'.upper())
                    user.balance += bets * 1.5
                    break

                turn = switch_turn(turn)
            elif turn == 'bust':
                turn = 'user'
                break

        user.player_deck.clear()
        computer.player_deck.clear()
        bets = 0
