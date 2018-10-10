import time

print("Welcome to the countdown!!!")

def countdown(con):
    while con >= 0:
        print(con)
        time.sleep(.9)
        con-=1

countdown(10)