#Author: Drew Rafferty
def getPrice():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid Number")

def getQuantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid Whole Number")


#Our Calculator
print("Our cost calculator")
price = getPrice()
quantity = getQuantity()
total = price * quantity
print(f"Your total is ${round(total,2)}")