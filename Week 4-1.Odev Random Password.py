
# Import edilecek kutuphaneler
from tkinter import *
import random, string

#Pencere Acilisi

root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("FT SIFRE OLUSTURUCU")

#Baslik
heading = Label(root, text = 'GENEL SIFRE' , font ='arial 15 bold').pack()
Label(root, text ='FATIH TURKMEN', font ='arial 15 bold').pack(side = BOTTOM)



###Sifre Uzunlugu Secimi
pass_label = Label(root, text = 'SIFRE UZUNLUGU', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 1, to_ = 10 , textvariable = pass_len , width = 15).pack()



#####Islev Tanimlamasi

pass_str = StringVar()

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
   


###Button Tanimlamasi

Button(root, text = "SIFRE OLUSTUR" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()





# loop to run program
root.mainloop()
