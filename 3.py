from random import randint

print("Bir sayi araligi girmeniz gerekiyor: ")
mini = int(input("1. sayiyi giriniz: "))
maxi = int(input("2. sayiyi giriniz: "))

# eger sayilari ters verirlerse diye, bir onemi yok ancak isimlendirme acisindan duzeltme gergi duydum
if mini > maxi:
    mini, maxi = maxi, mini

# bilgisayarin sectigi, oyunucun tahmin edecegi sayi
the_number = randint(mini,maxi)

# kac adimda buldugumuz
adim_sayisi = 1

while True:
    guess = int(input(f"{mini} - {maxi} Araliginda tahmin ediniz: "))

    if guess == the_number:
        print(f"Bildiniz!! {adim_sayisi} adimda buldunuz!!")
        break

    elif guess > maxi or guess < mini:
        print("Lutfen aralik dahili bir sayi tutunuz")

    elif guess < the_number:
        mini = guess
        print("Yukari")
        adim_sayisi += 1

    elif guess > the_number:
        maxi = guess
        print("Asagi")
        adim_sayisi += 1

