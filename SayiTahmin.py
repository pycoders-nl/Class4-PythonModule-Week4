

import random
import time

n = random.randint(1, 20)
tahmin = int(input("1 ve 20 arasinda bir sayi giriniz: "))
start_time = time.time()
count = 0

while n != "tahmin":
    count += 1
    if tahmin < n:
        print ("tahminin dusuk")
        tahmin = int(input("1 ve 20 arasinda bir sayi giriniz: "))
    elif tahmin > n:
        print ("tahminin yuksek")
        tahmin = int(input("1 ve 20 arasinda bir sayi giriniz: "))
    else:
        print ("Dogru!", int(time.time() - start_time), "saniyede ve", count, "ncu tahminde bildiniz...")
        #print  (int(time.time() - start_time), "saniyede bildiniz")
        break