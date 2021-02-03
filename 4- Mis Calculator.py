# As a user, I want to use a program which can calculate basic mathematical operations. So that I can add, subtract, multiply or divide my inputs.

# Acceptance Criteria:

#     The calculator must support the Addition, Subtraction, Multiplication and Division operations.
#     Define four functions in four files for each of them, with two float numbers as parameters.
#     To calculate the answer, use math.ceil()  and get the next integer value greater than the result
#     Create a menu using the print command with the respective options and take an input choice from the user.
#     Using if/elif statements for cases and call the appropriate functions.
#     Use try/except blocks to verify input entries and warn the user for incorrect inputs.
#     Ask user if calculate numbers again. To implement this, take the input from user Y or N.


import math
from addition import Addition
from subtraction import Subtraction
from multiplication import Multiplication
from division import Division
afronden = math.ceil


def num_input():
    while True:
        try:
            number = float(input("Please enter a float number: "))
            break
        except ValueError:
            print("""Please enter a valid float number using "." """)
    return number


def operant():
    while True:
        try:
            symbol = input("Please enter a mathematical operator symbol (+,-,*,/): ")
            if symbol != '+' and symbol != '-' and symbol != '*' and symbol != '/':
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid mathematical operator!")

    return symbol


def yes_no():
    while True:
        try:
            letter = input("Would you like to make another calculation (Y,N): ")
            if letter != 'Y' and letter != 'y' and letter != 'N' and letter != 'n':
                raise ValueError
            break
        except ValueError:
            print("Oops!  That was no valid symbol.  Try again...")

    return letter


while True:

    symbol = operant()

    if symbol == '+':
        print("Result: " + str(afronden(Addition(num_input(), num_input()))))
    elif symbol == '-':
        print("Result: " + str(afronden(Subtraction(num_input(), num_input()))))
    elif symbol == '*':
        print("Result: " + str(afronden(Multiplication(num_input(), num_input()))))
    elif symbol == '/':
        print("Result: " + str(afronden(Division(num_input(), num_input()))))

    antwoord = yes_no()
    if antwoord == 'N' or antwoord == 'n':
        break