#Author: Drew Rafferty
from datetime import date, time, datetime

reminders = {"Drop kids off at school": time(7, 50),
            "Pick up dry cleaning": time(8, 30),
            "Bake cookies for bake sale": time(10, 00),
            "Lunch with friends": time(12, 30),
            "Yoga": time(13, 15),
            "Pick up kids from school": time(14, 30),
            "Soccer practice": time(15, 15),
            "Dinner": time(17, 00),
            "Piano practice": time(18, 30),
            "Read books": time(19, 00),
            "Bed time": time(20, 00)}

counter = 0
for reminder in reminders:
    print (f"{counter}. " + reminder + " - " + reminders[reminder].strftime("%I:%M%p"))
    counter +=1
