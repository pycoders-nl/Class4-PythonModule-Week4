'''
3- Number Guessing Game

As a player, I want to play a game which I can guess a number the computer chooses in the range I chose. So that I can try to find the correct number which was selected by computer.
Acceptance Criteria:

Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
Your program should prompt the user for guesses
if the user guesses incorrectly, it should print whether the guess is too high or too low.
If the user guesses correctly, the program should print total time and total number of guesses.
You must import some required modules or packages
You can assume that the user will enter valid input.
'''

from random import randint
from time import time

target=randint(int(input('Lower Limit: ')),int(input('Upper Limit: ')))

print('Predict the Number:')
diff=time()
counter=0
while True:
    p=int(input())
    counter+=1
    if p==target:
        diff=time()-diff
        print(f'\nCongratulations!!!\nTarget Number is {target}',
              f'Number of Guesses: {counter}',
              f'Time Passed: {round(diff,1)} sec.',sep='\n')
        break
    else:
        if p > target: print('Too low...')
        else: print('Too high...')
        