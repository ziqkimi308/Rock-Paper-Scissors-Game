"""
********************************************************************************
* Project Name:  Rock Paper Scissors Game
* Description:   This is a simple Rock-Paper-Scissors game written in Python.
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

# Import
import random
from art import rock, paper, scissors

game_images = [rock, paper, scissors]

is_game = True
while is_game:
    choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

    if choose >= 3 or choose < 0:
        print("Invalid input!\n")
    else:
        print("You choose: ")
        print(game_images[choose])

        # Use random module randint
        comp_choose = random.randint(0,2)
        print("Computer choose: ")
        print(game_images[comp_choose])

        if choose == comp_choose:
            print("It's a draw.\n")
        elif comp_choose == 0 and choose == 2:
            print("You lose...\n")
        elif choose == 0 and comp_choose == 2:
            print("You win!\n")
        elif comp_choose > choose:
            print("You lose...\n")
        elif choose > comp_choose:
            print("You win!\n")