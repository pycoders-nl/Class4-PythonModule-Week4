import math


def least_common_multiple(num1, num2):
    gcd = math.gcd(num1, num2)

    return int((num1*num2) / gcd)


while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        break
    except ValueError:
        print('Please Enter a Number')

print(least_common_multiple(num1, num2))
