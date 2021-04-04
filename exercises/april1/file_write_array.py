#Author: Drew Rafferty

friends = ["amy", "bob", "carl", "dave"]

with open("exercises/april1/friends.txt","w") as file:
    for friend in friends:
        file.write(f"{friend}\n")