import random
import time

start_of_serie = int(input("Please enter your selected range's start:"))
end_of_serie = int(input("Please enter your selected range's end:"))
guess_count = 0
elapsed_time = 0
computer_selection = random.randint(start_of_serie, end_of_serie + 1)
# print(computer_selection)
start_time = time.time()
user_selection = int(input("Please guess a number from what was your selected range and insert: "))
guess_count += 1

while True:

    if user_selection == computer_selection:
        print("Congratulations")
        elapsed_time = time.time() - start_time
        print("Elapsed time: " + str(elapsed_time))
        print("Guess count: " + str(guess_count))
        break
    elif user_selection > computer_selection:
        user_selection = int(input("Please guess a smaller number than your guess: "))
        guess_count += 1
    else:
        user_selection = int(input("Please guess a bigger number than your guess: "))
        guess_count += 1
