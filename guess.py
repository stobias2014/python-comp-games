#!/bin/python3

import random

guesses_taken = 0
max_guesses = 6
print("Hello , whats is your name")
name = input()

number = random.randint(0, 20)

print("{0} I am thinking of a number betwee 0 - 20".format(name))

for guesses_taken in range(0, max_guesses):
    print("Take a guess")
    guess = int(input())

    if guess < number:
        print("Number is bigger than {0}".format(guess))
    elif guess > number:
        print("Number is less than {0}".format(guess))
    elif guess == number:
        break

if guess == number:
    print("You guessed my number in {0} guesses".format(guesses_taken))
    print("Your guess {0} is equal to number I was thinking {1}".format(guess, number))

if guess != number:
    print("Your guess {0} is not equal to number I was thinking of {1}".format(guess, number))


