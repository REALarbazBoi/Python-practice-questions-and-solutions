from datetime import *
# Counting months which starts from monday in a year
i = 1
count = 0
k = int(input("enter the year: "))
while i <= 12:
    c = date(k, i, 1)
    print(c.weekday())
    i += 1
    if c.weekday() == 0:
        count += 1

print("Number of month starting from Monday: ", count)


