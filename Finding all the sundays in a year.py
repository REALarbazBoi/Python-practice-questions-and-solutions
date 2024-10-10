import datetime as dt


def find_sun(num):
    first_day = dt.date(num, 1, 1)
    dw = first_day.weekday()
    days = dt.timedelta(6 - dw)

    sun = first_day + days
    count = 0
    while sun.year == num:
        print(sun)
        sun = sun + dt.timedelta(7)
        count += 1
    return count


print(find_sun(2024))