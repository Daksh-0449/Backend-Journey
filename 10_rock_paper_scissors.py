"""
Rock Paper Scissors
===================
A simple command-line Rock Paper Scissors game using
Enum, random, user input, and input validation.
"""

import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# Displaying Enum values
print(RPS(2))
print(RPS.ROCK)
print(RPS["ROCK"])

# Player input
player_choice = input(
    "Enter a choice (1 for rock, 2 for paper, 3 for scissors):

"
)

player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("Invalid choice, please try again")

# Computer choice
computer_choice = random.choice("123")
computer = int(computer_choice)

# Display choices
print()
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Computer chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print()

# Game result
if player == 1 and computer == 3:
    print("🥳 YOU WIN! 🥳")
elif player == 2 and computer == 1:
    print("🥳 YOU WIN! 🥳")
elif player == 3 and computer == 2:
    print("🥳 YOU WIN! 🥳")
elif player == computer:
    print("😮 GAME TIE 😮")
else:
    print("🐍 COMPUTER WINS!")
