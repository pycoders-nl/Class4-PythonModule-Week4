# As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers. So that I can find the least common multiple (L.C.M.) of my inputs.

# Acceptance Criteria:

# Ask user to enter the four numbers.
# Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
# Calculate the least common multiple (L.C.M.) of four numbers
# Use gcd function in module of math

import math

while True:
    try:
        my_list =[]

        for i in range(1,5):
            my_number = int(input("Enter a number for LCM: "))
            my_list.append(my_number)


        def gcd(my_list):
            result = my_list[0]
            for x in my_list[1:]:
                if result < x:
                    temp = result
                    result = x
                    x = temp
                while x != 0:
                    temp = x
                    x = result % x
                    result = temp
            return result 

        print(gcd(my_list))

    except:
        print("Please try again!")



