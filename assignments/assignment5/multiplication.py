#Author: Drew Rafferty

import random

print("Welcome to our muliplication game")
command = input("Shall we ask you a question (Y)es or (N)o?").lower().strip()

while command == "y":
    r1 = random.randint(1,10)
    r2 = random.randint(1,10)
    ans = r1*r2
    guess = int(input(f"{r1} * {r2} = "))
    if guess == ans:
        print("You got it!")
    else:
        print(f"Sorry, the correct answer is {ans}")
    command = input("Shall we ask you a question (Y)es or (N)o?").lower().strip()

    