"""
4- Mis Calculator

As a user, I want to use a program which can calculate basic mathematical operations. So that I can add, subtract, multiply or divide my inputs.
Acceptance Criteria:

The calculator must support the Addition, Subtraction, Multiplication and Division operations.
Define four functions in four files for each of them, with two float numbers as parameters.
To calculate the answer, use math.ceil() and get the next integer value greater than the result
Create a menu using the print command with the respective options and take an input choice from the user.
Using if/elif statements for cases and call the appropriate functions.
Use try/except blocks to verify input entries and warn the user for incorrect inputs.
Ask user if calculate numbers again. To implement this, take the input from user Y or N.
"""

import math
from operations import add, sum, multiply, divide

def isValid(n:str) ->bool:
    try:
        float(n)
    except Exception:
        print("Entry is invalid! Try again...\n")
        return False
    else:
        return True
while True:
    nums=[]
    while len(nums)<2:
        n=input(f"Number_{len(nums)+1}: ")
        if isValid(n): nums.append(int(n))

    while True:
        op=int(input('1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n\nSelect the operation number from the list above: '))
        if op in [1,2,3,4]: break
        print("Entry is invalid! Try again...\n")

    if op==1:
        result=add(nums[0],nums[1])
    elif op==2:
        result=sum(nums[0],nums[1])
    elif op==3:
        result=multiply(nums[0],nums[1])
    elif op==4 and nums[1] != 0:
        result=divide(nums[0],nums[1])

    operate = (op==1)*'+' or (op==2)*'-' or (op==3)*'*' or (op==4)*'/'
    print(f"{nums[0]} {operate} {nums[1]} = {math.ceil(result)}")
    
    if input('Do you want to continue? [y/n]:').lower()=='n':
        break