# 3- Number Guessing Game
# As a player, I want to play a game which I can guess a number the computer chooses in the range I chose. So that I can try to find the correct number which was selected by computer.

# Acceptance Criteria:

# Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
# Your program should prompt the user for guesses
# if the user guesses incorrectly, it should print whether the guess is too high or too low.
# If the user guesses correctly, the program should print total time and total number of guesses.
# You must import some required modules or packages
# You can assume that the user will enter valid input.

from random import randint # To choose a random number
import time # To calculate time

while True:
    try:

        begin_number = int(input("\nEnter te first number:\t")) # Enters e number for range
        end_number = int(input("\nEnter te first number:\t")) # Enters second number for range
        chosen_number = randint(begin_number,end_number) # Ramdomly choses a number
        total_try = 1 # Total try
        start_time = time.time() # Starting time

        while True:
            user_number = int(input("\nEnter your guess: ")) # Users guess
            if user_number == chosen_number:
                total_time = round(time.time() - start_time) # Totally spend time
                print("Congratulations! You find the right number after {} times! You spend total {} seconds!".format(total_try,total_time)) # Result
                print("Program starting again!") # Goes at the begining
                break
            elif user_number > chosen_number: # If number is high
                print("Your guess is higher than the Chosen number. Try to enter a lower number!")
                total_try += 1
            elif user_number < chosen_number: # If number is low
                print("Your guess is lower than the Chosen number. try to enter a higher number!")
                total_try += 1

            

    except:
        print("You entered foutive input! Please try again!")


