import math
from Addition import addition
from Subtraction import subtraction
from Multiplication import multiplication
from Division import division
round_number_ceil = math.ceil


def get_number_input():
    while True:
        try:
            number = float(input("Please enter a float ( with '.' ) number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return number


def get_operator_symbol():
    while True:
        try:
            symbol = input("Please enter a mathematical operator symbol (+,-,*,/): ")
            if symbol != '+' and symbol != '-' and symbol != '*' and symbol != '/':
                raise ValueError
            break
        except ValueError:
            print("Oops!  That was no valid symbol.  Try again...")

    return symbol


def get_y_n_answer():
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

    operator_symbol = get_operator_symbol()

    if operator_symbol == '+':
        print("Result: " + str(round_number_ceil(addition(get_number_input(), get_number_input()))))
    elif operator_symbol == '-':
        print("Result: " + str(round_number_ceil(subtraction(get_number_input(), get_number_input()))))
    elif operator_symbol == '*':
        print("Result: " + str(round_number_ceil(multiplication(get_number_input(), get_number_input()))))
    elif operator_symbol == '/':
        print("Result: " + str(round_number_ceil(division(get_number_input(), get_number_input()))))

    answer_letter = get_y_n_answer()
    if answer_letter == 'N' or answer_letter == 'n':
        break
