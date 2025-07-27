# Rock-Paper-Scissors Game in Python

import random

def get_user_choice():
    print("\nChoose one: rock, paper, scissors")
    return input("Your choice: ").lower()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

print("===== ROCK  PAPER  SCISSORS  =====")

while True:
    user_choice = get_user_choice()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue

    computer_choice = get_computer_choice()
    print(f" Computer chose: {computer_choice}")
    
    result = decide_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print(" Thanks for playing!")
        break
