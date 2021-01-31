#C@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@1
#   PyCoder Coding Class:4         @
#   Cabir Erguven                  @
#   Week        : 4                @
#   Question    : 3                @
#   Date: 30.01.2021               @
#C@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@1
#
#  Number Guessing Game
#
# Guess a number the computer chooses in the range I chose.
# So that I can try to find the correct number which was selected by computer.
#
# Acceptance Criteria:
#
#     Computer must randomly pick an integer from user selected a range,
#     i.e., from A to B, where A and B belong to Integer.
#     Your program should prompt the user for guesses
#     if the user guesses incorrectly, it should print whether the guess is too high or too low.
#     If the user guesses correctly, the program should print total time and total number of guesses.
#     You must import some required modules or packages
#     You can assume that the user will enter valid input.

from timeit import default_timer as timer
import random

print("******* GUESS THE NUMBER *******")
print("Enter the range of the number you want to find")

while True:
    try:
        begin = int(input("Enter the first number: "))
        finish = int(input("Enter the last number: "))
        break
    except ValueError:
        print("Please enter only number")


start = timer()
number = random.randint(begin, finish)
count = 0
guess =[]

while guess != number:
    count += 1

    try:
        guess = int(input("\nEnter your guess: "))
    except (ValueError, TypeError):
        print("Please enter a number")

    if guess > number:
        print(" It is too high")
    elif guess < number:
            print(" It is too low")
    else:
        print("\nCongratulation!!!")
        print("You guessed in",count,"times.")

end = timer()
print("It took", round((end - start), 2), "seconds to finish the game!")