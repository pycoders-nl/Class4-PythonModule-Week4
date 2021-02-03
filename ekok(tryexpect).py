sayi1 = int(input("Birinci Sayıyı Giriniz : "))
sayi2 = int(input("İkinci Sayıyı Giriniz : "))
if (sayi1>sayi2):
    kucuksayi = sayi2
else:
    kucuksayi = sayi1
for i in range(1,kucuksayi+1):
    if (sayi1 % i==0) and (sayi2%i ==0):
        ebob = i

print("Ekok = ", (sayi1*sayi2)//ebob)


try:
    sayi1= int(input("Birinci Sayıyı Giriniz :"))
    sayi2 = int(input("İkinci Sayıyı Giriniz : "))
    assert type(sayi1) == str
    assert type(sayi2) == str
except ValueError:
    print("lütfen sayı giriniz")

