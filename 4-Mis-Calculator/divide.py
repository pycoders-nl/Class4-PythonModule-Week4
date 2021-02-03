import math


def divide(num1, num2):
    return math.ceil(num1 / num2 if num1 > num2 else num2 / num1)
