'''
As a user, I want to use a program which can calculate basic mathematical operations.
So that I can add, subtract, multiply or divide my inputs.
Acceptance Criteria:
The calculator must support the Addition, Subtraction, Multiplication and Division operations.
Define four functions in four files for each of them, with two float numbers as parameters.
To calculate the answer, use math.ceil()  and get the next integer value greater than the result
Create a menu using the print command with the respective options and take an input choice from the user.
Using if/elif statements for cases and call the appropriate functions.
Use try/except blocks to verify input entries and warn the user for incorrect inputs.
Ask user if calculate numbers again. To implement this, take the input from user Y or N.
Author=Bulent Caliskan date=01/02/2021
'''
#We import the modules that need to be imported.
from math import ceil
#creat calculator function with ceil modul
# we also use try/except method for avoid mistakes
def calculator():
    while True:
       try:
            numbers=input("Enter the numbers you want to calculate(+/*-).Exmp= 4 + 5=> \n")
            numberSplit=numbers.split(" ")
            x,y,oparation=float(numberSplit[0]),float(numberSplit[2]),numberSplit[1]
            if oparation=="+":
                print(f"= {ceil(x+y)}")
            elif oparation=="-":
                print(f"= {ceil(x-y)}")
            elif oparation=="/":
                print(f"= {ceil(x/y)}")
            elif oparation=="*":
                print(f"= {ceil(x*y)}")
            else:
                print("You entered a wrong transaction.please dont forget space!")
                continue
       except:
            print("You entered a wrong transaction")
            continue
       yn = input("Do you want to continue. Y/N ")
       if yn == "Y" or yn == "y":
           continue
       else:break
# call the function
calculator()
