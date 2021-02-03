import random
import time

starting_point = int(input("type a starting point: "))
ending_point = int(input("type an ending point: "))
computer_guess = random.randint(starting_point, ending_point+1)
guess_counter = 0
guess_start_time = time.time()

while True:
    player_guess = int(input("guess a number: "))
    guess_counter += 1
    if player_guess == computer_guess:
        guess_end_time = time.time()
        duration = guess_end_time - guess_start_time
        print("player's guess is same with computer's guess\n" +
              "guessing amount: {}\n".format(guess_counter) + "guessing duration: {}\n".format(round(duration, 2)))
        break
    elif player_guess < computer_guess:
        print("player's guess is lower than computer's guess")
    elif player_guess > computer_guess:
        print("player's guess is higher than computer's guess")
