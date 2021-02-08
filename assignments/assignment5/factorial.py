#Author: Drew Rafferty

print("Welcome to our factorial generator")

num = int(input("Enter Number: "))
fact = 1

if num < 0:
    print("Does not exist")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print(f"Factorial of {num} is {fact} ")