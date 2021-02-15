"""
1 - Random Password
As a user, I want to use a program which can generate random password and display the result on user interface. So that I can generate my password for any application.

Acceptance Criteria:

Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
You must import some required modules or packages.
The GUI of program must contain at least a button and a label.
The result should be display on the password label when the user click the generate button.
"""

from tkinter import *
import random, string

def password_generator():
    password = []

    for i in range(4):
        password.append(random.choice(string.ascii_letters + string.digits))
    for i in range(2):
        password.append(random.choice(string.ascii_uppercase))
    for i in range(2):
        password.append(random.choice(string.digits))
    for i in range(2):
        password.append(random.choice(string.punctuation))

    random.shuffle(password)
    password = ''.join(password)

    return password

def start():
    while True:
        my_pass = password_generator()
        my_label.config(text=my_pass)
        break


my_app = Tk()
my_app.geometry("400x600")
my_app.title("Password Generator - Kerim")
my_button = Button(my_app, text="Create new password", command=start).pack(pady = 10)
my_label = Label(my_app, text="---Password---")
my_label.pack(pady=10)

my_app.mainloop()

