''''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210201]                                   ##
#*******************************************************************************************#
#############################################################################################
'''

n_loop = int(input("number of loop:"))
counter = 1
for i in range(n_loop):             # kac sayi girisi istendi ise onu sinirladim.
    counter = 1                     # bolunebilen digit leri tutmek icin. (son kalan digit zaten kendine bolunur)
    number = int(input("enter a number"))
    rest = number                   # manipuasyon yapmak icin sayinin kopyasini olusturdum. orjinal sayiyi korudum.
    while rest >= 10:               # kalan kisim tek haneli degilse, dongu devam eder.
        digit = rest % 10           # sayinin son(sag) basamagina ulastim.

        if digit == 0:              # sayinin son basamagi sifir ise bu bloga girer.
            rest = rest // 10       # sayinin son basamagindaki sifiri yok ettim. basamak sayisi azaldi.
        else:

            if number % digit == 0: # sayimiz digit e bolunebiliyor ise bu bloga girer.
                counter += 1        # count 1 artar.
                rest = rest // 10   # kalan sayinin son basamagini yok ettim.
            else:
                rest = rest // 10   # (sayimiz digit e tam bolunemiyorsa), kalan sayinin son basamagini yok ettim.
    print(counter)
