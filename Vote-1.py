import time

print("Welcome to the voting booth")\

time.sleep(.8)

print("Would you please enter your current age:")

time.sleep(.8)

myAge = input('')

if myAge >= '18':
    print('Please cast your vote')
else:
    print("Sorry, you're too young to vote.")