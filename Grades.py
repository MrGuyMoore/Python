import time

A = 93 - 100

B = 92.9 - 95.9
print("Welcome, Let's figure out your grade")

time.sleep(.8)

myGrade = int(float(input('Please enter your grade percent')))

time.sleep(.8)

if myGrade >= 93 and myGrade <= 100:
    print("Congratulations on your A!")
if myGrade <= 92.9 and myGrade >= 83:
    print('Congratulations on your B')
if myGrade <= 82.9 and myGrade >= 73:
    print('Congratulation on your C')
if myGrade <= 72.9 and myGrade >=65:
    print('Could have done better on your D')
else:
    if myGrade <= 64.9:
     print('Sorry, you failed this course.')
