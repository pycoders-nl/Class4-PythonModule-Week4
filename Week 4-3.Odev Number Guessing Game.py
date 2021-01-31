import random
import time

tahminler = 0
print('Lutfen isminizi giriniz....')
basla = time.time()

kullanicinin_ismi = input('Isim-Soyisim...:')
numara = random.randint(1, 20)
print(kullanicinin_ismi + ', Ben 1 ile 20 arasinda bir sayi tuttum')
while tahminler < 6:
    print('Benin tutdugum sayiyi bulmak icin bir tahmininde bulunurmusun....') # There are four spaces in front of print.
    tahmin = input('Tahmin griniz...:')
    tahmin = int(tahmin)
    tahminler = tahminler + 1
    if tahmin < numara:
        print('Senin tutdugun sayi benim tutdugum sayimdan dusuk.') # There are eight spaces in front of print.
    if tahmin > numara:
        print('Senin tutdugun sayi benim tutdugum sayimdan yuksek.')
    if tahmin == numara:
        break
if tahmin == numara:
    tahminler = str(tahminler)
    print('Harika, ' + kullanicinin_ismi + '! Tutdugum sayiyi buldunuz ' + tahminler + ' Tahminde!')
if tahmin != numara:
    numara = str(numara)
    print('HAYIR TAHMIN ETTIGIM SAYIYI BULAMADINIZ, tahmin ettigim sayi:' + numara)
son = int(time.time()-basla)
print("Toplam tahmin sureniz: {} Saniye".format(son))
