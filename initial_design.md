# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully

1. Output: "You are playing the Sticks game with two other players. The player who takes the last stick loses."
2. Prompt user for input: "Enter your name"
3. Prompt user for input: "Please enter the number of stick you would like to play with (between 10 and 100): "
4. Output: "Each player will take turns choosing 1,2, or 3 sticks"
5. Output: "The computer will randomly select a number of sticks from 1 to 3"
6. While total_sticks is > 1
   1. Prompt user for input: "How many sticks would you like to take (1,2, or 3)"
   2. Output: "There are ____ sticks left"
   3. Output: "The computer will now choose the amount of sticks to take"
      1. The computer will randomly select a number between 1 and 3
   4. Output: "There are _____ sticks left"
   5. Calculate the remaining total of sticks by: player_choice - total_sticks
      1. if total_sticks == "1"
         1. Output: "[current_player] left 1 stick and has the lost the game"
   6. Prompt user for input: "Would you like to play again (yes/no)?"
      1. If play_again != 'yes'
         1. break
   7. Output: "The game has concluded. The final scores were:"
      8. Search for which player had the most losses
         9. Output: "'Player' had lost 'total_losses' times."