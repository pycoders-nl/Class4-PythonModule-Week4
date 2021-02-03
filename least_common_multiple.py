import math

numbers = []
while True:
    if len(numbers) == 4:
        break
    else:
        try:
            number = int(input("type a number: "))
            numbers.append(number)
        except ValueError:
            print("your entry must be a number!")


def lcm(a, i):
    b = numbers[i]
    result = abs(a*b) // math.gcd(a, b)
    print(a, b, result)
    if i == len(numbers) - 1:
        return result
    else:
        i += 1
        return lcm(result, i)


result = lcm(numbers[0], 1)
print(result)
