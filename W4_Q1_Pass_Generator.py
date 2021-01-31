#C@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@1
#   PyCoder Coding Class:4         @
#   Cabir Erguven                  @
#   Week        : 4                @
#   Question    : 1                @
#   Date: 30.01.2021               @
#C@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@1
#
#  Random Password Generator
#
# Generate random password and display the result on user interface.
# So that I can generate my password for any application.
#
# Acceptance Criteria:
#
#     Password length must be 10 characters long.
#     It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
#     You must import some required modules or packages.
#     The GUI of program must contain at least a button and a label.
#     The result should be display on the password label when the user click the generate button.

import random
import tkinter as tk

def generate():
    names_upper = " ABCDEFGHIJKLMNOPRSTUVXYZ"
    names_lower = "abcdefghijklmnoprstuvxyz"
    spe_char = "!@$%&*_-+="
    digits ="1234567890"

    result_lower = random.sample(names_lower,3)
    result_upper = random.sample(names_upper,3)
    result_char = random.sample(spe_char,2)
    result_num = random.sample(digits,2)

    join_list = result_lower+result_upper+result_char+result_num
    random.shuffle(join_list)
    a = ("".join(join_list))

    message2 = tk.Label(root, text=a)
    message2.pack()


root = tk.Tk()
root.title("Password Generator")

# Instruction
message = tk.Label(root,text="  Please click the Generate button for your password  ")
message.pack()
root.geometry("300x350")

# Generate button
generateButton = tk.Button(root, bg="red", text="Generate", command=lambda:generate())
generateButton.pack()

root.mainloop()

