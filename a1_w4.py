''''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210201]                                   ##
#*******************************************************************************************#
#############################################################################################
'''

# 1 - Random Password
# As a user, I want to use a program which can generate random password and display the result on user interface.
# So that I can generate my password for any application.

# Acceptance Criteria:
# Password length must be 10 characters long.
# It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
# You must import some required modules or packages.
# The GUI of program must contain at least a button and a label.
# The result should be display on the password label when the user click the generate button.

import random
import tkinter

'''
ASCII karakter kodlarini referans alan, random karakter kodu listeleri olusturdum. 
sonra bu kodlari chr() metodu ile yazdirdim.
'''
table1 = tkinter.Tk()                                                   # passwordLabel table icin assign ettim.

def random_password():
    special_symbol_list = [random.randint(33, 47) for i in range(2)]    # 2 itemli random special_symbol_list olusturdum
    digits_list = [random.randint(48, 57) for i in range(2)]            # 2 itemli random digits_list olusturdum
    upper_case_list = [random.randint(65, 90) for i in range(2)]        # 2 itemli random upper_case_list olusturdum
    rest_list = [random.randint(97, 122) for i in range(4)]             # 4 itemli random rest_list olusturdum
    total_list = []                                                     # tum listeleri birlestirmek icin total_list.

    rest_list.extend(special_symbol_list)                               # iki listeyi birlestirdim.
    digits_list.extend(upper_case_list)                                 # iki listeyi birlestirdim.

    total_list.extend(rest_list)                                        # uc listeyi birlestirdim.
    total_list.extend(digits_list)                                      # dort listeyi birlestirdim.

    password = ''                                                       # password u tutmak icin bos string assign ettim.
    for i in range(10):
        password += chr(total_list[i])              # listedeki karakter kodlarini chr() ile karakter olarak birlestirdim.

    passwordLabel = tkinter.Label(table1, text=password, fg="white", bg="black", font="Verdana 19")
    passwordLabel.pack(fill=tkinter.X)
def main():
    table = tkinter.Tk()                                                # bir tkinter objesi olusturup table a atadim.
    table.title("Random Password Maker")                                # pencerenin basligini belirledim.
    table.geometry('999x400')                                           # boyutlarini belirledim.
    table.columnconfigure(0, weight=1)

    # table_Label
    label = tkinter.Label(table, text="Random Password Maker is Ready!", font=("Open Sans", "10", "bold"))
    label.pack()

    # acceptance_Criteria_Label
    criteriaLabel = tkinter.Label(table,
                                  text="Password will contain at least 2 upper case letter, 2 digits and 2 special symbols.")
    criteriaLabel.pack()

    # password_Button
    button = tkinter.Button(table, text="A Password Create", fg="orange", font=("Open Sans", "10", "bold"),
                            command=random_password)
    button.pack(padx=110, pady=70)
    table.mainloop()                                            # dongu olusturdum.

if __name__ == '__main__':                                      # bu dosya calisinca once main metodundan basla dedim.
    main()
