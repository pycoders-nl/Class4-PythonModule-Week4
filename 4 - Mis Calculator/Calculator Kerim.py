from Add_calculator import add
from Divide_calculator import divide
from Multiply_calculator import multiply
from Subtract_calculator import subtract

while True:
    try:
        entry = """
-------------------------      
1- Addition
2- Substraction
3- Multiplication
4- Division
        """
        print(entry)

        selection = int(input("Select the mathematical operation: "))
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        if selection == 1:
            print("\nResult is: " + str(add(first_number,second_number)))
        if selection == 2:
            print("\nResult is: " + str(subtract(first_number,second_number)))
        if selection == 3:
            print("\nResult is: " + str(multiply(first_number,second_number)))
        if selection == 4:
            print("\nResult is: " + str(divide(first_number,second_number)))

    except:
        print("Please try again!")