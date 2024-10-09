import datetime
import time


def age(dob):

    today = datetime.date.today()
    years = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        years -= 1

    return years

print("Age: ", age(datetime.date(1997,1, 20)))

