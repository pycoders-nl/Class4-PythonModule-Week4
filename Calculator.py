
import math

def add(num1, num2):
    return (math.ceil(num1 + num2))   # mathceil ile yuvarlamayi buradaki fonksiyonlarda yapiyorum
def subtract(num1, num2):
    return (math.ceil(num1 - num2))
def multiply(num1, num2):
    return (math.ceil(num1 * num2))
def divide(num1, num2):
    return (math.ceil(num1 / num2))

def calculate():        # hangi islemi yapacagimizi seciyoruz
    print("Please select the type of calculation -\n" \
          "1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n")

    while True:
        select = input("Select type of calculation 1, 2, 3, 4 :")
        try:
            assert 0 < int(select) < 5         #baska sayi ve rakam girislerinde uyarip tekrar ettiriyoruz
            break
        except:
            print("invalid entry!")
            continue
    while True:
        number_1 = input("Enter first number: ")
        number_2 = input("Enter second number: ")
        try:
            number_1 = float(number_1)         # rakam girilmezse uyarip tekrar ettiriyoruz
            number_2 = float(number_2)
            break
        except:
            print("invalid entries")
            continue
    if int(select) == 1:
        print(number_1, "+", number_2, "=", #islemine gore yukaridaki toplama, cikarrma vs fonsiyonlari cagiriyoruz
            add(number_1, number_2))

    elif int(select) == 2:
        print(number_1, "-", number_2, "=",
            subtract(number_1, number_2))

    elif int(select) == 3:
         print(number_1, "*", number_2, "=",
            multiply(number_1, number_2))

    elif int(select) == 4:
        try:
            assert number_2 != float(0)
        except :                                    # 0'a bolumde uyarip, bastan aliyoruz
            print("Ooops, ZeroDivisionError!!! ")
        else:
            print(number_1, "/", number_2, "=",
            divide(number_1, number_2))

    new_operation = input("Would you like a new calculation, key y/n: ")
    if new_operation == "y":
        calculate()
    elif new_operation == "n":                      # yeni islem yapmak istiyormuyuz
        input("\nPress the enter key to exit")
    else:
        print("Invalid entry byebye..")
calculate()
