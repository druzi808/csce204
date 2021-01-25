#Author: Drew Rafferty

print("Let's finish your room")
rWidth = float(input("Room Width: "))
rLength = float(input("Room Length: "))
rHeight = float(input("Room Height: "))
sFt = rWidth * rLength 
lengthXWidth = rLength * rWidth

floor = (rLength * rWidth) * 1.5
insulation = (rLength * rWidth) * 0.5
drywall = ((rLength * rWidth * 2) + ((rLength * rHeight * 2) * 4))
totalCost = floor + insulation + drywall


print(f"Room finishing cost: ${totalCost}")
