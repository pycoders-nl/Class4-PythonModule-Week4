# 2 - The Least Common Multiple

# As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers. So that I can find the least common multiple (L.C.M.) of my inputs.

# Acceptance Criteria:

#     Ask user to enter the four numbers.
#     Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
#     Calculate the least common multiple (L.C.M.) of four numbers
#     Use gcd function in module of math

import math
ebob = math.gcd


numbers = []                                      
ebob_list = []  
while True: 
    try: 
        number = input("Enter four numbers with spaces between them: ").strip(" ").split()
        for i in range(4):
            numbers.append(int(number[i])) 
        break
    except:
        print("Please enter only valid numbers!") 

ebob_list.append(ebob(numbers[0], numbers[1]))
ebob_list.append(ebob(numbers[2], numbers[3]))

ekok_list = [] 
n = 0
for i in range(2):
    i += i
    carpim = numbers[i] * numbers[i + 1]
    ekok_list.append(int(carpim / ebob_list[n]))
    n += 1
ebob_list2 = ebob(ekok_list[0], ekok_list[1])
ekok_result = ekok_list[0] * ekok_list[1]
result = ekok_result / ebob_list2                      # sonucta istenen okek i result a atatim.
print("The Least Common Multiple of {},{},{},and {} is ---{}---"
      .format(numbers[0], numbers[1], numbers[2], numbers[3], int(result)))