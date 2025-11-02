#Guess the number game

import random

guess = 0
number = random.randint(1, 10)

print("Welcome to the Guess the Number Game!")

for attempt in range(5):
    print("Take a guess betweeen 1 and 10")
    guess = int(input())

    if guess < number :
        print("Too low!")
    elif guess > number:
        print("Too high!")   
    else:
        break

if guess == number:
    print("Congratulations! You guessed the correct number ", number)
else:
    print("Sorry, the number was", number)    