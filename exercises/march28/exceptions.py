#Author: Drew Rafferty
try:
    number = int(input("Enter number: "))
except ValueError:
    print("You entered an invalid integer")