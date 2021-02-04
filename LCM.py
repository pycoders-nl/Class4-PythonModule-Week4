

from math import gcd

while True:
    print ("Enter 4 number please,")
    num1 = input ("Enter number 1: ")
    num2 = input ("Enter number 2: ")
    num3 = input("Enter number 3: ")
    num4 = input("Enter number 4: ")
    try:
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        num4 = int(num4)
        break
    except ValueError:               # sayi girilmez ise uyarip, tekrar ettiriyoruz
        print("invalid entries")
        continue

a = [num1, num2, num3, num4]
print ("Entered Numbers :", a)
lcm = a[0]
for i in a[:]:
  lcm = lcm*i//gcd(lcm, i)
print("The L.C.M. of :", num1, '-', num2,'-', num3,'-', num4,  "is", lcm )

