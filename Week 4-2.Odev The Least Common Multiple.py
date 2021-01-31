import math
while(True):
    try:
        num_1 = int(input('num_1:'))
        num_2 = int(input('num_2:'))
        num_3 = int(input('num_3:'))
        num_4 = int(input('num_4:'))
        okek = math.lcm(num_1, num_2, num_3, num_4)

        print('L.C.M.....=', okek)
        break
    except (ValueError):
        print('lUTFEN GIRISLERINIZI TEKRAR YAPINIZ YANLIS DEGER GIRDINIZ.......')










