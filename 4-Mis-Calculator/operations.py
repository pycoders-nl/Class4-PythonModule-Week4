from add import add
from subtract import subtract
from multiply import multiply
from divide import divide


while True:
    operation = ''
    try:
        op = input(
            'Enter the operation you want to do (A: Addition, S: Subtraction, M: Multiplication, D: Division ): ')
        if op.lower() == 'a':
            operation = 'Addition'
        elif op.lower() == 's':
            operation = 'Subtraction'
        elif op.lower() == 'm':
            operation = 'Multiplication'
        elif op.lower() == 'd':
            operation = 'Division'
        else:
            print('Enter the right value')
            continue

        num1 = int(input('Enter the first number to do {} : '.format(operation)))
        num2 = int(input('Enter the second number to do {} : '.format(operation)))
    except ValueError:
        print('Please enter an appropriate input to the place')
        continue

    if operation.lower() == 'addition':
        print(add(num1, num2))
    elif operation.lower() == 'subtraction':
        print(subtract(num1, num2))
    elif operation.lower() == 'multiplication':
        print(multiply(num1, num2))
    elif operation.lower() == 'division':
        print(divide(num1, num2))

    try:
        again = input("Do you want to do another calculation? (Y or N): ")
        if again.lower() != 'y' or again.lower() != 'y':
            print('Your answer must be either Y or N. It is note case sensetive.')
            print('Starting the progress again. Please enter the right value')
            continue
    except:
        print('There was an error try again')

    if again.lower() == 'y':
        print("Starting again")
        continue
    elif again.lower() == 'n':
        break
    else:
        print('')
