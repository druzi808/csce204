#Author: Drew Rafferty

temp = int(input("Enter Temperature: "))
percip = input("enter (R)ain, (S)now, or (N)one: ").lower().strip()

if temp <= 40 and percip == "s":
    print("you need a snowsuit")
elif temp <= 40 and percip == "r":
    print("you need a sweater and a rain jacket")
elif temp <= 40:
    print("you need to dress in layers")