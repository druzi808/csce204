#Author: Drew Rafferty
import random

def play_game(get_players_choice, get_comp_choice):
    compScore = 0
    playerScore = 0

    if get_players_choice == get_comp_choice:
        print("It's a tie!")
        return 0

    elif get_players_choice == 1:
        if get_comp_choice == 2:
            print("Computer Wins") 
            compScore += 1
        else:
            print("Player Wins")
            playerScore += 1
    elif get_players_choice == 2:
        if get_comp_choice == 3:
            print("Computer Wins")
            compScore += 1
        else:
            print("Player Wins")
            playerScore += 1
    elif get_players_choice == 3:
        if get_comp_choice == 1:
            print("Computer Wins")
            compScore += 1
        else:
            print("Player Wins")
            playerScore += 1
    print(f"Computer Total Wins: {compScore}")
    print(f"Player Total Wins: {playerScore}")


def get_players_choice():
    player_choice = input("Enter (R)ock, (P)aper, or (S)cissors: ").lower().strip()
    if player_choice == "r":
        return 1
    elif player_choice == "p":
        return 2
    elif player_choice == "s":
        return 3

def get_comp_choice():
    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        print ("Computer used Rock")
        return 1
    elif comp_choice == 2:
        print ("Computer used Paper")
        return 2
    elif comp_choice == 3:
        print ("Computer used Scissors")
        return 3



#Program

print("Welcome to  Rock Paper Scissors")

while True:
    begin = input("""(P)lay or (Q)uit: """).lower().strip()
    if begin == "q":
        break
    elif begin == "p":
        get_players_choice()
        get_comp_choice()
        play_game(get_players_choice, get_comp_choice)


    
