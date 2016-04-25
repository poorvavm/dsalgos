# Number guessing game in python:
import random
# create a random number
getNumber = random.randint(1,101)

# get guess
guess = int(input("enter number:"))
guesscounter = 1
# check if high low or increment decrement the guess
while (guess!= getNumber):
    if guess > getNumber:
        print ("number is less then : "+str(guess))
    else:
        print ("number is greater then : "+str(guess))
    guesscounter += 1
    guess = int(input("enter number:"))
# print the guess counter
print (" gess and getNumber are same")
print guesscounter
