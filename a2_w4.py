''''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210202]                                   ##
#*******************************************************************************************#
#############################################################################################
'''

# 2 - The Least Common Multiple.
# As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers.
# So that I can find the least common multiple (L.C.M.) of my inputs.

# Acceptance Criteria:

# Ask user to enter the four numbers.
# Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
# Calculate the least common multiple (L.C.M.) of four numbers
# Use gcd function in module of math.

import math

numbers_list = []                                       # kullanicidan alinan 4 sayiyi listede tutmak icin.
gcd_compute = []                                        # obeb lerini tutmak icin.
while True:                                             # hatali giris yapildigi surece donmesi icin.
    try:                                                # hatali girisleri yakalamak icin.
        numbers = input("Enter 4 numbers with spaces between them: ").strip(" ").split() # str tutan numbers list olusur.
        for i in range(4):
            numbers_list.append(int(numbers[i]))        # girilen sayilari int tutan numbers_list e ekledim.
        break # hatali giris yoksa while dongusunu kirdim.
    except:
        print("Please only enter numbers!")             # hatali girislerde bu mesaj goruntulenir.

gcd_compute.append(math.gcd(numbers_list[0], numbers_list[1])) # gcd() kullararak ilk iki sayinin obeb ini hesapladim.
gcd_compute.append(math.gcd(numbers_list[2], numbers_list[3])) # gcd() kullararak son iki sayinin obeb ini hesapladim.

LCM_list = []                                           # sayilarin okek ini tutmak icin
j = 0                                                   # gcd_compute listesi item lerine ulasmak icin.(obeb)
for i in range(2):
    i += i
    multiple = numbers_list[i] * numbers_list[i + 1]    # numbers_list teki ilk iki ve sonra son iki sayi carpimi.
    LCM_list.append(int(multiple / gcd_compute[j])) # ilk iki sayinin carpimlarini obeb ine boldum. sonucu listede tuttum.
    j += 1
gcd_compute2 = math.gcd(LCM_list[0], LCM_list[1])       # yeni olusan iki sayinin da gcd() ile obeb lerini hesapladim.
LCM_result = LCM_list[0] * LCM_list[1]                  # yeni olusan iki sayiyi carptim.
result = LCM_result / gcd_compute2                      # sonucta istenen okek i result a atatim.
print("The Least Common Multiple of {},{},{},and {} are --> {} <--"
      .format(numbers_list[0], numbers_list[1], numbers_list[2], numbers_list[3], int(result)))
