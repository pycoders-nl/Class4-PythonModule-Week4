"""
As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers.
So that I can find the least common multiple (L.C.M.) of my inputs.

Acceptance Criteria:

Ask user to enter the four numbers.
Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
Calculate the least common multiple (L.C.M.) of four numbers
Use gcd function in module of math
"""
# Python program to find LCM of four numbers wíth use gcd functon in module of math
from math import gcd
numlist = []
for x in range(4):
    while True:
        try:
            a = int(input("Enter four numbers to calculate their LCM: "))
            break
        except ValueError:
            print("You entered non numerical, please enter the number correctly")

    numlist.append(a)

# Function to return LCM of two numbers


def lcm(a, b):
    return int((a / gcd(a, b)) * b)
# Function to return LCM of four numbers


def lcm4(t, x, y, z):
    return lcm(lcm(lcm(t, x), y), z)


print('LCM of', numlist, 'is', lcm4(numlist[0], numlist[1], numlist[2], numlist[3]))
