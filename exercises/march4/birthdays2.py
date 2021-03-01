#Author: Drew Rafferty
from datetime import date, time, datetime

birthdays = {"Amy": date(2021, 3, 22),
             "Bobby": date(2021, 3, 22),
             "Carl": date(2021, 3, 22),
             "Dave": date(2021, 3, 22),
             "Erin": date(2021, 3, 22),
             "Fred": date(2021, 3, 22),
             "Gretta": date(2021, 3, 22)}


closestBirthday = date(2021, 12, 31)
closestFriend = ""

for friend in birthdays:
    birthday = birthdays[friend]
    daysTillBirthday = (birthday - date.today()).days
    daysTillCurrentClosest = (closestBirthday - date.today()).days
    #if bday occured
    if daysTillBirthday < 0:
        continue
    if(daysTillBirthday < daysTillCurrentClosest):
        closestBirthday = birthday
        closestFriend = friend
    
print("The closest birthday is "+ closestFriend +" " + closestBirthday.strftime("%m/%d/%y"))
