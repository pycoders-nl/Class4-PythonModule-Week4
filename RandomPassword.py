''''
As a user, I want to use a program which can generate random password and display the result on user interface.
So that I can generate my password for any application.

Acceptance Criteria:

Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
You must import some required modules or packages.
The GUI of program must contain at least a button and a label.
The result should be display on the password label when the user click the generate button.
Author= Bulent Caliskan  date= 31/01/2021
'''
import tkinter as tk

import random

# Function for calculation of password
def passFunc():
    entry.delete(0, 'end')

    length=10
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789!@#$%^&*()"
    password = ""
    for i in range(0,3):
        password=password+random.choice(lower)
    for i in range(0,3):
        password = password + random.choice(upper)
    for i in range(0,4):
        password = password + random.choice(digits)
    ps=set(password)
    return "".join(ps)
# Function for generation of password
def button():
    password1=passFunc()
    entry.insert(10,password1)

# main function
randompass=tk.Tk()
# Title of your GUI window
randompass.title("Random Password 1.1")
randompass.geometry("400x200")

# create label and entry to show
# password generated
rpLabel=tk.Label(randompass,text=" Press the button to generate a random password ",bg="white")
rpLabel.pack(pady=20)

passView = tk.Label(randompass, text=" Password ",fg="green",font=("Open Sans","10","bold"))
passView.pack(pady=1)

entry = tk.Entry(randompass,text= passFunc)
entry.pack(pady=10)

# create Button
button =tk.Button(randompass, text = " GENARATE ",width=15,height =2,fg="green",command=button)
button.pack(pady=5)

# start the GUI
randompass.mainloop()



