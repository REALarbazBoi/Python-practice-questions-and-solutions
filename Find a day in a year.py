import datetime as dt
import time

today = dt.date(2024,1,1)
dt1 = dt.date(2024,10,11)

diff_date = dt1 - today
new_date = today + dt.timedelta(diff_date.days)
print(diff_date)
print(new_date)