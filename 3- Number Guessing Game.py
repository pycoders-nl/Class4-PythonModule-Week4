# 3- Number Guessing Game

# As a player, I want to play a game which I can guess a number the computer chooses in the range I chose. So that I can try to find the correct number which was selected by computer.

# Acceptance Criteria:

#     Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
#     Your program should prompt the user for guesses
#     if the user guesses incorrectly, it should print whether the guess is too high or too low.
#     If the user guesses correctly, the program should print total time and total number of guesses.
#     You must import some required modules or packages
#     You can assume that the user will enter valid input.

import random
import time


minimum = int(input("Please enter the minimum number: "))
maximum = int(input("Please enter the maximum number: "))
target = random.randint(minimum, maximum)

print("The computer has the number chosen.")

n = 1  

time1 = time.time()
while True:
    predict = int(input("Your guess: "))
    if predict == target:
        print("Congratulations!")
        break                                                
    elif predict > target:  
        print("Please try a smaller number: ")
        n += 1
    elif predict < target:
        print("Please try a bigger number: ")
        n += 1
    continue  
time2 = time.time() 
duration = float(time2 - time1)

print("Elapsed time: {} seconds". format(duration))
print("Number of tries: {}". format(n))
