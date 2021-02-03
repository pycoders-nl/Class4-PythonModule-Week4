import random
import time


def guess_my_number():
    start = time.time()
    while True:
        try:
            min_range_to_guess = int(input("enter the min amount:"))
            max_range_to_guess = int(input("enter the max amount:"))
            if(min_range_to_guess >= max_range_to_guess):
                print("Min value must be lower than max value")
                continue
            break
        except ValueError:
            print("Please enter a number")

    computer_number = random.randint(
        min_range_to_guess, max_range_to_guess)
    num_guess = 0
    print(computer_number)
    lower = min_range_to_guess
    higher = max_range_to_guess

    while True:
        guess = int(
            input("Guess a number between {} and {}: ".format(lower, higher)))

        if guess > higher or guess < lower:
            print("your guess must be between given range")
            continue

        num_guess += 1

        if computer_number < guess:
            print('Your  guess is higher than my number. You shold guess lower.')
            higher = guess
            continue
        elif computer_number > guess:
            print('Your  guess is higher than my number. You shold guess lower.')

            lower = guess
            continue
        elif computer_number == guess:
            end = time.time()
            print("Conguratulations!!! Your guess was right.")
            print("You guessed my number in {} times. it took you {} seconds to find my number.".format(
                num_guess, int(end - start)))
            break


guess_my_number()
