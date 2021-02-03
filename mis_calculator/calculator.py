import math
import addition
import subtraction
import multiplication
import division

result = 0
operations = ["1", "2", "3", "4"]

while True:
    operation = input(
        "addition: 1\nsubtraction: 2\nmultiplication: 3\ndivision: 4\n\nchoose an operation: ")
    if operation not in operations:
        print("type a valid operation!\n")
    else:
        while True:
            try:
                a = float(input("type a number: "))
                b = float(input("type a number: "))
                break
            except ValueError:
                print("type a valid number!\n")
        if operation == "1":
            result = addition.addition(a, b)
        elif operation == "2":
            result = subtraction.subtraction(a, b)
        elif operation == "3":
            result = multiplication.multiplication(a, b)
        elif operation == "4":
            result = division.division(a, b)

        if type(result) == str:
            print(result)
        else:
            print(math.ceil(result))
        yes_or_no = input(
            "\nfor a new operation, type 'Y'.\nto exit, type 'N'. \nyour choice: ")
        while yes_or_no.upper() != "Y" and yes_or_no.upper() != "N":
            print("type 'Y' or 'N'!")
            yes_or_no = input(
                "\nfor a new operation, type 'Y'.\nto exit, type 'N'. \nyour choice: ")
        if yes_or_no.upper() == "N":
            print("bye!")
            break
        elif yes_or_no.upper() == "Y":
            continue
