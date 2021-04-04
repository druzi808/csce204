#Author: Drew Rafferty

numbers = [8, 16, 43, 87] 

with open("exercises/april1/numbers.txt","w") as file:
    for number in numbers:
        #file.write(f"{number}\n")
        file.write(str(number) + "\n")