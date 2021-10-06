import datetime
from datetime import date
import calendar


def find(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


i = 0
while i < 2:
    day = input()
    month = input()
    year = input()
    date = day + " " + month + " " + year
    day = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thrusday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    key_list = list(day.keys())
    val_list = list(day.values())
    if find(date) in val_list:
        position = val_list.index(find(date))
        print(key_list[position])
    i += 1
