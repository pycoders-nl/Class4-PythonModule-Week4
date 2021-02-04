
import random
import string
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.title("Password Generator App")
root['background']='#856ff8'
root.geometry("450x450")


pass_str = StringVar()
def generate():      # 2'ser tane  buyuk harf, rakam ve karakteri seciyoruz, toplam 6 ediyor
    random_source = string.ascii_letters + string.digits + string.punctuation
    password =  random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
    password += random.choice(string.digits) + random.choice(string.digits)
    password += random.choice(string.punctuation) + random.choice(string.punctuation)

    for i in range(4):          #kalan 4 karakteri yukaridaki kumeden aliyorum
        password += random.choice(random_source)

    pass_str.set(password)


Label(root, text="Password Generator Application", font="Lucida 20 bold").pack()

Button(root, text="Generate Password",  command=generate).pack(pady=7)

Entry(root, textvariable=pass_str).pack(pady=2)
root.mainloop()

