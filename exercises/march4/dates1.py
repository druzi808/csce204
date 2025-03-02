import random

from datetime import date, time, datetime

todaysDate = date.today()

print(todaysDate)
print(todaysDate.strftime("%m/%d/%y"))
print(todaysDate.strftime("%A %B %d, %Y"))

todaysDateTime = datetime.now()

print(todaysDateTime)
print(todaysDate.strftime("%A %B %d, %Y: %I:%M%p"))

halloween = date(2021, 10, 31)
meeting = time(14, 30) #2:30
appointment = datetime(2021, 3, 1, 17, 30) #march 1 2021 2:30

#birthdate program - use for contact
dateEntered = input("Enter birthday (MM/DD/YYYY):").strip()
birthDate = datetime.strptime(dateEntered, "%m/%d/%Y")

print("Your birthday is " + birthDate.strftime("%B %d"))

#how long until appt
days = (appointment - datetime.now()).days
print(f"You have {days} days till your appointment")