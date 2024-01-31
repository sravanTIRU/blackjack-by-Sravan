# blackjack-by-Sravan
A traditional blackjack game with custom rules.

This is the game where user gets to interact with the computer unlike the war card game,
where only two computer objects fight with each other.

this might not be the perfect implementation of the code.
i am still in the learning phase with python and decided to make somethin fun with it.

# enjoy the game...

# here are thet game rules.

Blackjack Game Rules:

Objective:
The goal of the game is to beat the computer opponent by having a hand value closer to 21 without exceeding it.

Setup:
- Each round starts with the player (user) and the computer receiving two cards each.
- The deck is shuffled at the beginning of each round.
- The player places a bet before the round starts.

Game Flow:

1. Player's Turn:

   - The player has the following commands:
   
     - 1: Show Hand - Displays the cards in the player's hand.
     - 2: Check Balance - Shows the current balance of the player.
     - 3: Hit - Draws a new card and adds it to the player's hand.
     - 4: Stay - Ends the player's turn.
     - 5: Show Bets - Displays the current bets on the table
     - 6: !!!WARNING!!! PROGRAM IMMEDIATELY TERMINATES. USE WITH CAUTION.⚠️

   - The player can continue hitting until they choose to stay, reach 21, or bust (exceed 21).
   - If the player wins (reaches 21), they receive 1.5 times their bet. If the player busts, they lose the round.

2. Computer's Turn:

   - The computer plays according to a basic strategy:
     - It continues to draw cards until its hand value is at least 17.
   - The computer may win, lose, or tie with the player.
   - If the player wins or ties, the player receives the corresponding winnings.

3. Round Result:
   - The winner of the round is determined based on hand values:
     - If the player's hand value is closer to 21 without exceeding it, the player wins.
     - If the computer's hand value is closer to 21 without exceeding it, the computer wins.
     - If both have the same hand value, the round ends in a tie.

Game Over:
- The game continues until the player decides to quit or runs out of the minimum required balance.
- The minimum required balance to continue playing is 300.

Betting:
- The player can bet using increments of 100, with a maximum bet of 500.

Good luck, and may the cards be in your favor!

