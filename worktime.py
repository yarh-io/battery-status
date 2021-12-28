#
import time
import datetime

print("===")
with open ('time.txt', 'a') as f:
    f.write ("===\n")
while True:
    with open ('time.txt', 'a') as f:
        f.write (datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S\n"))
    print(datetime.datetime.now())
    time.sleep(60)
