"""
WAs a player, I want to play a game which I can guess a number the computer chooses in the range I chose.
So that I can try to find the correct number which was selected by computer.

Acceptance Criteria:

Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
Your program should prompt the user for guesses
if the user guesses incorrectly, it should print whether the guess is too high or too low.
If the user guesses correctly, the program should print total time and total number of guesses.
You must import some required modules or packages
You can assume that the user will enter valid input.
"""
import random
from time import time

print("******************************************************\n"
      "***               Quess the number                 ***\n"
      "******************************************************")
print("Enter the range of the game")

while True:
    try:
        low_lim = int(input('Please Enter Lower Limit of Prediction: '))
        upp_lim = int(input('Please Enter Upper Limit of Prediction: '))
        break
    except ValueError:
        print("Please enter only number")

t_time = time()
number = random.randint(low_lim, upp_lim)
counter = 0
guess = []
print("***I'm ready. Guess my number***")
while guess != number:
    counter += 1
    try:
        guess = int(input("\nEnter your guess: "))
    except (ValueError, TypeError):
        print("Please enter a number")

    if guess > number:
        print("Try again! It is Too high...")
    elif guess < number:
        print("Try again! It is Too low...")
    else:
        print("\nCongratulation!!!")
        print("My Number is", number)
        print("Total number of your guesses, ", counter)
        t_time = time() - t_time
        print("Total time of your guesses, ", round(t_time, 1), "seconds")
