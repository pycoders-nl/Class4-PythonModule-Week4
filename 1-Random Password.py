import random
import string
from tkinter import *


def password_generator():
    result = ""
    for i in range(1, 11):
        result = result + random.choices(
            string.ascii_uppercase + string.digits + string.punctuation + string.ascii_lowercase).pop()

    return result


def is_suitable_password(password):
    upper_case_count = 0
    lower_case_count = 0
    digit_count = 0
    symbol_count = 0

    for i in password:
        if string.ascii_lowercase.count(i) > 0:
            lower_case_count += 1
        elif string.ascii_uppercase.count(i) > 0:
            upper_case_count += 1
        elif string.punctuation.count(i) > 0:
            symbol_count += 1
        else:
            digit_count += 1

    if digit_count >= 2 and upper_case_count >= 2 and symbol_count >= 2:
        return True
    else:
        return False


def press():
    while True:

        new_password = password_generator()
        if is_suitable_password(new_password) is True:
            l1.config(text=new_password)
            break


main_frame = Tk(className=" Password Generator App")
main_frame.geometry("400x400")
b1 = Button(main_frame, text="Generate password", command=press).pack()
l1 = Label(main_frame, text="Welcome")
l1.pack()

main_frame.mainloop()
