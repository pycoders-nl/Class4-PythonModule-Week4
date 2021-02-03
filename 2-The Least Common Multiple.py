import math
gcd = math.gcd

while True:
    try:
        a = int(input("Please enter first number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
while True:
    try:
        b = int(input("Please enter second number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

while True:
    try:
        c = int(input("Please enter third number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

while True:
    try:
        d = int(input("Please enter fourth number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

print("L.C.M. is : " + str(gcd(a, b, c, d)))
