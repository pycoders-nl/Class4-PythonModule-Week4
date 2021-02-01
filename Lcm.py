''''
****The Least Common Multiple****
As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers.
So that I can find the least common multiple (L.C.M.) of my inputs.
Acceptance Criteria:
Ask user to enter the four numbers.
Use blocks to verify input entries and warn the user for Nan or non numerical inputs.try/except
Calculate the least common multiple (L.C.M.) of four numbers
Use gcd function in module of math
Author= Bulent Caliskan  date=31/01/2021
'''
import math as m
# put the 4 numbers we get from the user into a list.
def numberList():
    x=1
    number_list=[]
    while x<5:
        try:
            numbers=int(input(f"Enter {x}. number which you want to calculate "
                  "\nthe least common multiple?"))
            number_list.append(numbers)
            x+=1
        except:
            print("You did not enter a number ")
            continue
    return number_list
numbersList=numberList()
#creat GCM for 4 numbers
def gcm():
    number_gcm=numbersList
    glm1=m.gcd(number_gcm[0] , number_gcm[1])
    glm2=m.gcd(glm1 , number_gcm[2])
    glmFourNumbers=m.gcd(glm2 , number_gcm[3])
    return  glmFourNumbers
# creat LCM for 4 numbers and use math.gcd() modul
def lcm():
    number_lcm=numbersList
    lcm1=int((number_lcm[0]*number_lcm[1])/(m.gcd(number_lcm[0],number_lcm[1])))
    lcm2=int(lcm1*number_lcm[2]/(m.gcd(lcm1,number_lcm[2])))
    lcmFourNumbers= int(lcm2*number_lcm[3]/(m.gcd(lcm2,number_lcm[3])))
    return lcmFourNumbers
print(f"LCM of your 4 numbers {lcm()}") # call the LCM function

print(f"GCM of your 4 numbers {gcm()}")# call the GCM function