# GAME 1
import random

def play_game():
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    user_action = input("Enter a choice: Rock, Paper, or Scissors: ")

    if user_action not in possible_actions:
        print("Invalid input, please try again.")
    else:
        print("The computer chose " + computer_action)
        if user_action == computer_action:
            print("It's a tie!")
        elif (user_action == "rock" and computer_action == "scissors") or \
            (user_action == "paper" and computer_action == "rock") or \
            (user_action == "scissors" and computer_action == "paper"):
            print("You win!")
        else:
            print("You lose!")

play_game()



