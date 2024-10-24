# Programmers: Jordi Campoverde
# Course: CS151, Dr.Yalew
# Due Date: 10/24/24
# Programming Assignment: 2
# Problem Statement: To create a sticks game for 2 players and a computer
# Data In: The total number of sticks they want to play, the total number of sticks they decide to take each time from 1-3 sticks
# Data Out: The total number of sticks left, The total losses of each player if they decide to stop playing the game
# Credits: Created with the help of notes taken from class

import random

def sticks_game():
    print("You are playing the Sticks game with two players and a computer.The player who takes the last stick loses.")
    # To establish that there are 3 players in the game
    player1 = input("Enter your name (Player 1): ")
    player2 = input("Enter your name (Player 2): ")

    # Initialize player losses
    player_losses = {player1: 0, player2: 0, "Computer": 0}

    while True:  # Allow multiple games
        # Prompt for the total number of sticks (between 10 and 100)
        total_sticks = int(input("Please enter the number of sticks you would like to play with (between 10 and 100): "))
        while total_sticks < 10 or total_sticks > 100:
            print("Please enter a number between 10 and 100.")
            total_sticks = int(input("Please enter the number of sticks you would like to play with (between 10 and 100): "))

        print("Each player will take turns choosing 1, 2, or 3 sticks.")

        # List of players including computer
        players = [player1, player2, "Computer"]
        current_player_idx = 0

        # Game loop
        while total_sticks > 1:
            current_player = players[current_player_idx]

            if current_player != "Computer":
                # Player's turn
                player_choice = int(input(f"{current_player}, how many sticks would you like to take (1, 2, or 3)? "))
                while player_choice < 1 or player_choice > 3 or player_choice >= total_sticks:
                    print(f"Please enter a valid number (1, 2, or 3) less than the remaining sticks ({total_sticks}).")
                    player_choice = int(
                        input(f"{current_player}, how many sticks would you like to take (1, 2, or 3)? "))

                total_sticks -= player_choice
                print(f"There are {total_sticks} sticks left.")

                if total_sticks == 1:
                    print(f"{current_player} left 1 stick and lost the game.")
                    player_losses[current_player] += 1
                    break

            else:
                # Computer's turn
                computer_choice = random.randint(1,3)
                if computer_choice >= total_sticks:
                    computer_choice = total_sticks - 1

                total_sticks -= computer_choice
                print(f"The computer took {computer_choice} stick(s).")
                print(f"There are {total_sticks} sticks left.")

                if total_sticks == 1:
                    print("Computer left 1 stick and lost the game.")
                    player_losses["Computer"] += 1
                    break

            # Move to the next player
            current_player_idx = (current_player_idx + 1) % 3

        # Prompts the player if they want to play again
        play_again = input("Would you like to play again (yes/no)? ").strip().lower()
        if play_again != 'yes':
            break

    # Final output for the total number of losses
    print("The game has concluded. The final scores were:")
    for player, losses in player_losses.items():
        print(f"{player} lost {losses} time(s).")


# Start the game
sticks_game()

