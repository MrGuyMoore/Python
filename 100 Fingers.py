import time

print("Let's count those fingers!!!")

myFinger = 0

for myFin in range(1, 101):
    myFinger=2**myFin
    print(myFinger)
    time.sleep(.8)