#Author: Drew Rafferty

print("Welcome to our grocery store")
print(f"The following items are in the store: ")

groceries = ["apples", "bananas", "pears", "grapes", "kiwis"]

for grocerie in groceries:
    print(grocerie)

order = input("What would you like to order? ")
if order == "apples":
    groceries.remove("apples")
    print(f"We've ordered {order} for you")
elif order == 'bananas':
    groceries.remove("bananas")
    print(f"We've ordered {order} for you")
elif order == "pears":
    groceries.remove("pears")
    print(f"We've ordered {order} for you")
elif order == "grapes":
    groceries.remove("grapes")
    print(f"We've ordered {order} for you")
elif order == "kiwis":
    groceries.remove("kiwis")
    print(f"We've ordered {order} for you")
else:
    print(f"Sorry we don't have any {order}")

print("Now the grocery store has the following: ")

for grocerie in groceries:
    print(grocerie)
print("Goodbye")
#toys.append("phone")
#toys.remove("truck")