from math import ceil

def addition(x, y):
    print(ceil(float(x) + y))
def subtraction(x, y):
    print(ceil(float(x) - y))
def multiplication(x, y):
    print(ceil(float(x) * y))
def division(x, y):
    print(ceil(float(x) / y))

while True:
    while True:
        try: 
            islem = int(input("""Yapmak istediginiz islemi seciniz (Yapmak istediginiz islemin numarasini yazin): 
        1) Toplama
        2) Cikarma
        3) Carpma
        4) Bolme
        """))
            if islem < 1 or islem > 4:
                print("Lutfen gecerli bir islem seciniz!")
                continue
            break
        except:
            print("Lutfen bir islem seciniz!")


    while True:
        try: 
            sayi1 = int(input("Birinci sayiyi giriniz: "))
            sayi2 = int(input("Ikinci sayiyi giriniz: "))
            break
        except:
            print("Gecerli bir sayi girmediniz!")


    if islem == 1: addition(sayi1, sayi2)
    elif islem == 2: subtraction(sayi1, sayi2)
    elif islem == 3: multiplication(sayi1, sayi2)
    elif islem == 4: division(sayi1, sayi2)

    if input("Islem yapmaya devam etmek istiyor musunuz? (Y)/(N)") == "N":
        break
