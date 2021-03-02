#Author: Drew Rafferty

from datetime import date, time, datetime

holidays = {"Valentine's Day": date(2021, 2, 14),
            "St. Patrick's Day": date(2021, 3, 17),
            "Easter": date(2021, 4, 4),
            "Memorial Day": date(2021, 5, 31),
            "July 4th": date(2021, 7, 4),
            "Labor Day": date(2021, 9, 6),
            "Thanksgiving": date(2021, 11, 25),
            "Christmas": date(2021, 12, 25)}

closestHoliday = date(2021, 12, 31)
closestDate = ""

for holiday in holidays:
    hDate = holidays[holiday]
    daysTilHoliday = (hDate - date.today()).days
    daysTillCurrentClosest = (closestHoliday - date.today()).days
    if daysTilHoliday < 0:
        closestHoliday = hDate
        closestDate = holiday
        print(holiday + " - " + closestHoliday.strftime("%m/%d/%y") + " Passed")
    elif daysTilHoliday == 0:
        closestHoliday = hDate
        closestDate = holiday 
        print(holiday + " - " + closestHoliday.strftime("%m/%d/%y") + " TODAY!")
    elif daysTilHoliday <= 30 and daysTilHoliday > 0:
        closestHoliday = hDate
        closestDate = holiday 
        print(holiday + " - " + closestHoliday.strftime("%m/%d/%y") + " only 12 days away")
    else:
        print(holiday + " - " + closestHoliday.strftime("%m/%d/%y"))
