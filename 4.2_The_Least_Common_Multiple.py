"""
2 - The Least Common Multiple

As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers. So that I can find the least common multiple (L.C.M.) of my inputs.

Acceptance Criteria:

Ask user to enter the four numbers.
Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
Calculate the least common multiple (L.C.M.) of four numbers
Use gcd function in module of math
"""
from math import gcd

def isValid(n:str) ->bool:
    try:
        1/int(n)
    except Exception:
        print("Entry is invalid! Try again...\n")
        return False
    else:
        return True

nums=[]
while len(nums)<4:
    n=input(f"Number_{len(nums)+1}: ")
    if isValid(n): nums.append(int(n))
        
gcd1 = gcd(nums[0],nums[1])
gcd2 = gcd(nums[2],nums[3])
lcm_1 = nums[0]*nums[1] // gcd1
lcm_2 = nums[2]*nums[3] // gcd2

print(f"\nEBOB{nums} = {gcd(gcd1,gcd2)}\n"
      f"EKOK{nums} = {lcm_1*lcm_2//gcd(lcm_1,lcm_2)}")