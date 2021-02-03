import tkinter
import random
import string
from tkinter.constants import BOTTOM, CENTER, RAISED

upper_letter = string.ascii_uppercase
lower_letter = string.ascii_lowercase
digit = string.digits
symbol = string.punctuation
all_randoms = upper_letter + lower_letter + digit + symbol

top = tkinter.Tk()
top.title("password generator")
top.geometry("400x400")
var = tkinter.StringVar()
password_label = tkinter.Label(
    top, textvariable=var, relief=RAISED, width=20, height=5)


def generator():
    uppers = random.choices(upper_letter, k=2)
    digits = random.choices(digit, k=2)
    symbols = random.choices(symbol, k=2)
    rest_of_password = random.choices(all_randoms, k=4)
    raw_password = uppers + digits + symbols + rest_of_password
    random.shuffle(raw_password)
    password = "".join(raw_password)
    print(password)
    var.set("password: " + password)
    password_label.pack()


button = tkinter.Button(top, text="generate",
                        command=generator, width=20, height=5)
button.pack()
top.mainloop()
