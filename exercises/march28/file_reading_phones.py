#Author: Drew Rafferty

def getPhoneBook():
    phonebook = {}
    with open("exercises/march28/phones.txt") as file:
        for line in file:
            data = line.split(',')
            friend = data[0].strip()
            phoneNumber = data[1].strip()
            phonebook[friend] = phoneNumber
        return phonebook
def getPhone(phoneList):
    friend = input("Enter Persons Name: ").lower().strip()
    if friend in phoneList:
        print(f"{phoneList[friend]}")
    else:
        print(f"Sorry {friend} is not in our system")

print("Displaying Phone Book")
phoneList = getPhoneBook()
for person in phoneList:
    print(f"{person}: {phoneList[person]}")

getPhone(phoneList)