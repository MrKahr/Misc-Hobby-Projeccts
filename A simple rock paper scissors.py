# Al Sweigart, the author of Automate the Boring Stuff with Python, inspired this script.

#  Create a simple rock paper scissors programme.
#  It should
#  1. Track wins losses and draws (compare computer and human moves)
#  2. Give the user the ability to quit the programme
#  3. Should print a human readable output of each choice and the comparison between them

import random  # the computer has to pick rock, paper of scissors
import sys  # we want to create an exit
import time  # we want to create pauses
# Note: I know I can import multiple library with a single expression.
# This is an attempt to make the code more readable.

wins = 0
losses = 0
draws = 0
while True:
    # main game starts here
    # intro
    print("Welcome to another game of rock, paper scissors!")
    # tally
    print("The current score is ", wins, 'wins ', losses, 'losses and', draws, 'draws.\n')
    while True:
        # The user chooses a move
        user_move = input("If you'd like to play against the computer, please select r,p,s or q to quit\n")
        if user_move == "q":
            sys.exit()
        elif user_move == "r" or "p" or "s":
            break
        elif user_move != "r" or "p" or "s" or "q":  # NOT FUNCTIONAL ERROR, BUT THE PROGRAMME WORKS
            print("This input is not allowed, please select another")
    if user_move == "r":
        print("You have chosen rock!")
    elif user_move == "p":
        print("You have chosen paper!")
    elif user_move == "s":
        print("You have chosen scissors!")
    # Computer chooses a move
    possible_computer_moves = ["r", "p", "s"]
    computer_move = random.choice(possible_computer_moves)
    if computer_move == "r":
        print("The computer chose...")
        time.sleep(1.5)
        print("rock!")
        time.sleep(1)
    elif computer_move == "p":
        print("The computer chose...")
        time.sleep(1.5)
        print("paper!")
        time.sleep(1)
    elif computer_move == "s":
        print("The computer chose...")
        time.sleep(1.5)
        print("scissors!")
        time.sleep(1.5)
    # Compare the moves and add the tally to the result
    if user_move == computer_move:
        print('Its a draw!\n')
        draws += 1  # less readable way to write draw = draw + 1
        time.sleep(1.5)
    elif user_move == "r" and computer_move == "p":
        print("You lose!\n")
        losses += 1
        time.sleep(1.5)
    elif user_move == "r" and computer_move == "s":
        print("You Win!\n")
        wins += 1
        time.sleep(1.5)
    elif user_move == "p" and computer_move == "s":
        print("You Lose!\n")
        losses += 1
        time.sleep(1.5)
    elif user_move == "p" and computer_move == "r":
        print("You Win!\n")
        wins += 1
        time.sleep(1.5)
    elif user_move == "s" and computer_move == "r":
        print("You Lose!\n")
        losses += 1
        time.sleep(1.5)
    elif user_move == "s" and computer_move == "p":
        print("You Win!\n")
        wins += 1
        time.sleep(1.5)
