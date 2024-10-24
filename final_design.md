# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 

1. import random
2. Output: "You are playing the Sticks game with two players and a computer. The player who takes the last stick loses."
3. Prompt player 1 for input: "Enter your name (Player 1): "
4. Prompt player 2 for input: "Enter your name (Player 2): "
5. Prompt for the total number of sticks: "Please enter the number of sticks you would like to play with (between 10 and 100): "
   1. Validate the input: Ensure the number is within the range (10-100).
6. Output: "Each player will take turns choosing 1, 2, or 3 sticks."
total_sticks = user input
player_losses = {player1: 0, player2: 0, "Computer": 0}.
current_player starting with player1.
7. While total_sticks is greater than 1:
   1. If current_player is a player (Player 1 or Player 2):
      1. Prompt the player: "How many sticks would you like to take (1, 2, or 3)? " 
      2. Subtract the player's choice from the total sticks
      3. Output: "There are ____ sticks left"
      4. If total_sticks equals to 1:
         1. Output:"[current_player] left 1 stick and lost the game."
         2. player_losses[current_player] += 1
   2. break the loop
   3. If current_player = computer:
      1. Use random int (1,3)
      2. Subtract total sticks by the amount the computer chose 
      3. "The computer took ____ sticks. There are ____ sticks left."
      4. If total_sticks equals to 1:
         1. Output: "Computer left 1 stick and lost the game."
         2. player_losses["Computer"] += 1
   4. break the loop
8. Prompt the user for input: "Would you like to play again (yes/no)?"
   1. If the decision doesnt equal yes:
      2. break 
9. Output: "The game has finally ended. The scores are:"
10. Use for loop to list all the player losses
    1. Output: (f"{player} lost {losses} times.")
        