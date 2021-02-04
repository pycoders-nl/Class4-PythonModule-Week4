"""
As a user, I want to use a program which can generate random password and display the result on user interface.
So that I can generate my password for any application.

Acceptance Criteria:
Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
You must import some required modules or packages.
The GUI of program must contain at least a button and a label.
The result should be display on the password label when the user click the generate button.
"""
import random
import string
import tkinter as tk


def gen_pass(lenght=10):
    letters = string.ascii_lowercase
    up_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    passlist = random.sample(letters, 4)+random.sample(up_letters, 2)+random.sample(digits, 2)+random.sample(symbols, 2)
    password = ''.join(random.sample(passlist, lenght))  # her deger 1 kere kullanilir
    # password = ''.join(random.choice(passlist) for i in range(lenght)) # her deger 1 den fazla denk gelebilir yada gelmeyebilir
    label2 = tk.Label(root, text='Your Password :  '+password+'\n', fg="black", )
    label2.pack()


root = tk.Tk()
root.title("Password Generator")

# Information
label1 = tk.Label(root, text="  Please click the button for generate your password  \n")
label1.pack()
# root.geometry("400x350") #ana pencere boyutu ayarlanabilir yada veri girisi ile otomatik genisler

# Password Generate button
PassGenButton = tk.Button(root, bg="DeepSkyBlue2", fg="black", text="Generate My Password", command=lambda: gen_pass())
PassGenButton.pack()

root.mainloop()
