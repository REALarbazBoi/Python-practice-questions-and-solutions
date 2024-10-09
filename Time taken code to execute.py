import datetime
import time

start_time = time.time()
for i in range(100000000):
    pass
end_time = time.time()
total_time = end_time - start_time
print(total_time)


start_time = datetime.datetime.now()
for i in range(100000000):
    pass
end_time = datetime.datetime.now()

total_time = end_time - start_time
print(f"total time is {total_time.seconds} seconds and {total_time.microseconds} microseconds ")