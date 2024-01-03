# python minigame, rock, paper, scissors
# rock beats scissors
# scissors beats paper
# paper beats rock

import random


def play():
    """Play a game of rock, paper, scissors"""

    # get the player's and computer's total wins and the total rounds
    total_rounds = 0
    computer_wins = 0
    player_wins = 0
    play_the_game = True
    
    while play_the_game:

        # the player can choose one of three options(rock, paper, scissors) 
        player = input("What's your choice? Rock, paper or scissors.\n").lower()
        computer = random.choice(['rock', 'paper', 'scissors'])

        # warning if the player doesn't choose one of the three options
        if player not in ['rock', 'paper', 'scissors']:
            print("Invalid input, try again")
            continue

        # the player get's informed about the computer's choice and the result of the round
        print(f"Computer chose {computer}")
        if player == computer:
            print("It's a tie.")
        elif is_win(player, computer):
            player_wins += 1
            print("You won!")
        else:
            computer_wins += 1
            print("You lost!")
        player_choice = input("Do you want to continue or quit the game? (continue/quit)\n")
        if player_choice == "continue":
            continue
        elif player_choice == "quit":
            if computer_wins > player_wins:
                print(f"You have {player_wins} wins. You lost the game!")
            else:
                print(f"You have {player_wins} wins. You won the game!")
            play_the_game = False

def is_win(player, computer):
    """Return true if player wins"""
    # rock beats scissors
    # scissors beats paper
    # paper beats rock
    if (player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
        return True

play()
