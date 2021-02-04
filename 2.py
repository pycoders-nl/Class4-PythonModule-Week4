from math import gcd

s = list()
i = 1

while i < 5:
    temp = input(f"{i}. sayiyi giriniz: ")
    try:
        s.append(int(temp))
        i+=1
    except ValueError:
        print("Bir sayi yazar misin lutfen")
    except:
        print("Unexpected error:", sys.exc_info()[0])

sol = 1
for i in s:
    sol = (sol * i) // gcd(sol, i) 

print(sol) 