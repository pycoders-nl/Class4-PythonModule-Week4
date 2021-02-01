''''
As a player, I want to play a game which I can guess a number the computer chooses in the range I chose.
So that I can try to find the correct number which was selected by computer.
Acceptance Criteria:
Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
Your program should prompt the user for guesses
if the user guesses incorrectly, it should print whether the guess is too high or too low.
If the user guesses correctly, the program should print total time and total number of guesses.
You must import some required modules or packages
You can assume that the user will enter valid input.
4- Mis Calculator
Author=Bulent Caliskan date 01/02/2021
'''
#We import the modules that need to be imported.
import random
from timeit import default_timer as timer
#start the game time
start = timer()
#creat guessFunc function with random modul
def guessFunc():
    print("Enter two numbers and try to guess the number to choose between. ")
    a,b=int(input("Enter first number")),int(input("Enter second number"))
    number=random.randint(a,b)
    move = 0
    while True:
        move+=1
        guess=int(input("Guess the number I kept "))
        if number < guess:
            print("You should enter a smaller number than your guess. ")
            continue
        elif number> guess:
            print("You should enter a bigger number than your guess. ")
            continue
        else:
            #finish the game time and return result with f string
            end = timer()
            return print(f"Congratulations, you got the correct guess in {end-start:.3} second and {move} times. ")
#call the function
guessFunc()