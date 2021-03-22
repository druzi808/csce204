#Author: Drew Rafferty
import random

def play_game(get_players_choice, get_comp_choice):
    if get_players_choice == get_comp_choice:
        return 0

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
player_score = 0
comp_score = 0
print("Welcome to  Rock Paper Scissors")
While True:

    begin = input("""(P)lay or (Q)uit""").lower().strip()
    if begin == "q":
        break
    
