from math import ceil
def toplama():
    x = a + b 
    print(x)

def cikarma():
    x = a - b 
    print(x)

def bolme():
    x = a / b
    print(x)

def carpma():
    x = a * b 
    print(x)
while True:
    try:
        a = ceil(float(input('Lutfen birinci sayi giriniz: ')))
        b = ceil(float(input('Lutfen ikinci sayiyi giriniz: ')))
        c = int(input('Toplama icin "1"e , Cikarma icin "2", Bolme icin "3", Carpma icin"4" , Cikis icin "0"a basiniz: '))
        if c == 1:
            toplama()
        elif c ==2:
            cikarma()
        elif c ==3:
            bolme()
        elif c==4:
            carpma()
        elif c==0:
            print('Iyi gunler')
            break
    except ZeroDivisionError:
        print('Lutfen bolme yaparken ikinci sayiyi 0 girmeyiniz...')
        

