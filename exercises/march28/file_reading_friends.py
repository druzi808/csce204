#Author: Drew Rafferty
def getFriends():
    friends = []
    with open("exercises/march28/friends.txt") as file:
        for line in file:
            friend = line.replace("\n", "")
            friends.append(friend)
        return friends

people = getFriends()
        
print("See my friends: ")
for i in range(len(people)):
    print(f"{i+1}. {people[i]}")
