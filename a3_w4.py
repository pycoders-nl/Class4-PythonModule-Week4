''''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210202]                                   ##
#*******************************************************************************************#
#############################################################################################
'''
# 3- Number Guessing Game
# As a player, I want to play a game which I can guess a number the computer chooses in the range I chose.
# So that I can try to find the correct number which was selected by computer.

# Acceptance Criteria:
# Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
# Your program should prompt the user for guesses
# if the user guesses incorrectly, it should print whether the guess is too high or too low.
# If the user guesses correctly, the program should print total time and total number of guesses.
# You must import some required modules or packages
# You can assume that the user will enter valid input.

import random
from time import time

print('%' * 56)
print("%%%%%%%%[+  The Number Guessing Game Begins!  +]%%%%%%%%")
print('%' * 56)
min_n = int(input("enter a min integer number for Number Guessing Game:"))  # min sayiyi aldim.
max_n = int(input("enter a max integer number for Number Guessing Game:"))  # max sayiyi aldim.
chosen_number = random.randint(min_n, max_n)                                # girilen araliktan bir sayi secti computer.
print("the computer chose a number..")
n = 1                                                           # tahmin sayisini tutmak icin
t1 = time()                                                     # sureyi baslattim.
while True:                                                     # hatali tahmin girilirse dongu devam eder.
    guess = int(input("your guess: "))                          # oyuncudan tahmini ni aldim.
    if guess == chosen_number:                                  # random belirlenen ile oyuncunun tahmin sayisi esitse.
        print("[[Congratulations! Your {}. guess!".format(n))   # game over, sonucu yazdirdim
        break                                                   # oyuncu bildi ise while dan cikar.
    elif guess > chosen_number:                                 # tahmin daha buyukse, yonlendirdim.
        print("try a smaller number:")
        n += 1
    elif guess < chosen_number:                                 # tahmin daha kucukse, yonlendirdim.
        print("try a bigger number:")
        n += 1
    continue                                                    # tahmin dogru degilse while in basina doner.
t2 = time()                                                     # oyuncu bildi ise while dan cikar. sureyi durdurdum.
elapsed = t2 - t1                                               # fark alip gecen sureyi hesapladim.
print('Elapsed time is %f seconds.]]' % elapsed)
