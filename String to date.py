import datetime

class MyError(Exception):
    pass


try:
    a = input("enter date in DD-MM-YY format: ")
    d, m, y = a.split("-")

    d1 = datetime.date(int(y), int(m), int(d))
    print(d1)

except:
    raise MyError("Sahi value daal nahi to value error aajayega")