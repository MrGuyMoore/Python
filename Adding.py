import time, math


print("Welcome, let's do some adding!")

time.sleep(.9)

print("Let's start by entering some numbers")

time.sleep(.9)

print("Please enter your first number:")

time.sleep(.9)

numOne = input('')

time.sleep(.9)

print("Please enter your second number:")

time.sleep(.9)

numTwo = input('')

sum = float(numOne) + float(numTwo)

if sum <= 100:
    print("They add up to {0}" .format(sum))
else:
    print("They add up to a big number")
