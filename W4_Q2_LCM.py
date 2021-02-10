#C@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@1
#   PyCoder Coding Class:4         @
#   Cabir Erguven                  @
#   Week        : 4                @
#   Question    : 2                @
#   Date: 30.01.2021               @
#C@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@1
#
# Calculate the least common multiple (L.C.M.) of four numbers.
# So that I can find the least common multiple (L.C.M.) of my inputs.
#
# Acceptance Criteria:
#
#     Ask user to enter the four numbers.
#     Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
#     Calculate the least common multiple (L.C.M.) of four numbers
#     Use gcd function in module of math

import math
list = []
res = 1
a = 0


for x in range(4):
    while True:
        try:
            a = int(input("Enter four numbers to calculate their LCM: "))
            break
        except ValueError:
            print("You entered NaN, please enter the numbers correctly")


    list.append(a)

lcf_step1 = int((list[0] * list[1]) / math.gcd(list[0], list[1]))   # recursive can be used
lcf_step2 = int((lcf_step1 * list[2]) / math.gcd(lcf_step1, list[2]))
lcf_step3 = int((lcf_step2 * list[3]) / math.gcd(lcf_step2, list[3]))

print("LCF of", list[0], list[1], list[2], list[3], "is:", lcf_step3)
