#Author: Drew Rafferty

weekDay = input("Enter weekday: ").lower().strip()

if weekDay == "monday" or weekDay == "mon":
    print("Moes Monday")
elif weekDay == "tuesday" or weekDay == "tues":
    print("Taco Tuesday")
elif weekDay == "wednesday":
    print("Wine Wednesday")
else: 
    print ("No deals today")