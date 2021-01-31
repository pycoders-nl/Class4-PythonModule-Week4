#C@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@1
#   PyCoder Coding Class:4         @
#   Cabir Erguven                  @
#   Week        : 4                @
#   Question    : 4                @
#   Date: 30.01.2021               @
#C@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@1
#
# Mis Calculator
#
# A program which can calculate basic mathematical operations.
# So that I can add, subtract, multiply or divide my inputs.
#
# Acceptance Criteria:
#
#     The calculator must support the Addition, Subtraction, Multiplication and Division operations.
#     Define four functions in four files for each of them, with two float numbers as parameters.
#     To calculate the answer, use math.ceil()  and get the next integer value greater than the result
#     Create a menu using the print command with the respective options and take an input choice from the user.
#     Using if/elif statements for cases and call the appropriate functions.
#     Use try/except blocks to verify input entries and warn the user for incorrect inputs.
#     Ask user if calculate numbers again. To implement this, take the input from user Y or N.

import math
import add_of_calculator as a, subtract_of_calculator as s, multiply_of_calculator as m, divide_of_calculator as d
while True:
    operation_list = ["+","-","*", "/"]
    operation = input("Which operation do you want to perform ' + - * / ' ?")

    if operation not in operation_list:
        print("Operation is INVALID! \nEnter only the following symbols ' + - * / ' ")
        break
    try:
        first = int(input("enter first number: "))
        second = int(input("enter second number: "))
    except (ValueError, NameError):
        print("Please Enter only number")
        break

    if operation == "+":
        print("The result is: ",math.ceil(a.add(first,second)))
    elif operation == "-":
        print("The result is: ",math.ceil(s.subtract(first,second)))
    elif operation == "*":
        print("The result is: ",math.ceil(m.multiply(first,second)))
    elif operation == "/":
        print("The result is: ",math.ceil(d.divide(first,second)))

    answer = input("\nDo you want to perform more operation? [Y /N]")
    if answer == ("n" or "N"):
        print ("See you again! ")
        break

