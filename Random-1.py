import time, random

randomNum = random.randint(0,100)

guessesTaken = 0

time.sleep(.1)

print('Welcome to the Random Number Game.')

time.sleep(.8)

print('Please enter your name:')

time.sleep(.7)

myName = input('')

print(myName+" let us get started on the game.")

time.sleep(.8)

while guessesTaken == 0:
    print('Please pick a number, any number!!!')
    time.sleep(.9)
    guess = input()
    guess = int(guess)

    if guess < randomNum:
        print('Sorry, number is too low')
        time.sleep(.8)

    if guess > randomNum:
        print('Sorry, number is too high')
        time.sleep(.8)
    if guess == randomNum:
        break

if guess == randomNum:
    print("Well done on guessing the number!!!")



