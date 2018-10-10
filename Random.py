import time, random, atexit

randomNum = random.randint(0,9)

guessesTaken = 0

time.sleep(.1)

print('Welcome to the Random Number Game.')

time.sleep(.8)

print('Please enter your name:')

time.sleep(.7)

myName = input('')

print(myName+" let us get started on the game.")

while guessesTaken < 3:
    print('Please pick a number, any number')
    time.sleep(.9)
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1
    if guess < randomNum:
        print('Please try again')
        time.sleep(.8)

    if guess > randomNum:
        print('Please try again')
        time.sleep(.8)
    if guess == randomNum:
        break

if guess == randomNum:
    print("Well done on guessing the number!!!")



