import datetime as dt


def prev_day(day):

    week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    today = dt.datetime.today()
    t_dw = today.weekday()
    dw = week_days.index(day)

    diff = dw - t_dw

    if diff < 0:
        new_date = today + dt.timedelta(diff)

    else:
        new_date = today + dt.timedelta(-(7-diff))

    return new_date


print("Today : ", dt.datetime.today())
print("Prev: ", prev_day("thursday"))