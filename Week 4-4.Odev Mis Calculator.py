import toplama as tp
import cikarma as ck
import bolme as bl
import carpma as cr
print("Lutfen yapmak istediginiz islemi seciniz.......")
print("1.Toplama")
print("2.Cikarma")
print("3.Carpma")
print("4.Bolme")
while True:
    secim = input("Lutfen yapiniz (1/2/3/4): ")
    try:
        if secim in ('1', '2', '3', '4'):
            num1 = float(input("Ilk sayiyi giriniz: "))
            num2 = float(input("Ikinci sayiyi giriniz: "))
            if secim == '1':
                topla=tp.tpl.toplama(num1,num2)
                print(num1, "+", num2, "=", topla)
            elif secim == '2':
                cikar = ck.ckm.cikarma(num1, num2)
                print(num1, "-", num2, "=",cikar )
            elif secim == '3':
                carp = cr.crp.carpma(num1, num2)
                print(num1, "*", num2, "=", carp)
            elif secim == '4':
                bol = bl.blm.bolme(num1, num2)
                print(num1, "/", num2, "=", bol)
        else:
            print("Yanlis secim lutfen tekrar deneyiniz...............")

        tercih=input('Baska islem yapmak icin x e cikmak icin y ye basiniz......:')
        if tercih=='y':
            print('Isleminiz sona ermistir.........')
            break
        elif tercih=='x':
            continue
        else:
            tercih=input('Baska islem yapmak icin x e cikmak icin y ye basiniz......:')




    except (ValueError):
        print('lUTFEN GIRISLERINIZI TEKRAR YAPINIZ YANLIS DEGER GIRDINIZ.......')











































