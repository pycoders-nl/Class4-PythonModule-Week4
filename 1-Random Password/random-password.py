import tkinter as tk
import random
import string
from tkinter import ttk


def main():
    global password
    root = tk.Tk()
    root.title("This is a random password generator")
    root.geometry("300x300")
    root.columnconfigure(0, weight=1)

    # Password Label
    pass_label = tk.Label(root, text="Your Password is")
    pass_label.grid()

    # Password
    password = tk.Label(root, text="", fg='green')
    password.grid()

    # create Password
    create_pass = tk.Button(
        root, text="Generate Password", command=generate)
    create_pass.grid()

    # foorter
    footer = tk.Label(root, text="Created By Abuzer ALACA")
    footer.grid()

    root.mainloop()


def generate():
    global password
    passw = []
    passw = passw + random.sample(list(string.ascii_lowercase), k=4)
    passw = passw + random.sample(list(string.ascii_uppercase), k=2)
    passw = passw + random.sample(list(string.punctuation), k=2)
    passw = passw + random.sample(list(string.digits), k=2)
    random.shuffle(passw)

    passsw = ''.join(passw)

    password.config(text="\""+passsw+"\"")


if __name__ == "__main__":
    main()
