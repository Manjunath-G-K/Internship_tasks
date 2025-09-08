
# Task 1: Number Guessing Game
# Student: Manjunath G K
# Date: 07/09/2025

import random
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 20. Can you guess it?")

secret_number = random.randint(1, 20)
attempts = 0
maximum_attempts = 5

while attempts < maximum_attempts:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        attempts = attempts + 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts!")
            break
    else:
        print("Please enter a valid number.")

if attempts == maximum_attempts and guess != secret_number:
    print("Sorry! You used all attempts. The number was", secret_number, "Try again!!!")
