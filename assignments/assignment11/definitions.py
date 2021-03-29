#Author: Drew Rafferty
def getDictionary():
    definitions = []

    try:
        with open("assignments/assignment11/words.txt") as file:
            for line in file:
                definition = line.replace("\n", "")
                definitions.append(definition)
    except:
        print("File could not be located")

    return definitions

def displayDictionary(dictionary):
    defin = getDictionary()
    for dictionary in defin:
        print(dictionary)

while True:
    command = input("Would you like to (V)iew, (D)efine, or (Q)uit: ").lower().strip()

    if command == "q":
        print("Goodbye")
        break
    elif command == "v":
        displayDictionary
    elif command == "d":
        getDictionary()
    

