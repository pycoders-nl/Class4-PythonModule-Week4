import tkinter as tk
from random import random, shuffle


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        tk.Button(self, command = self.generate_cipher, text = "Generate Cipher").pack()

        tk.Button(self, text="QUIT", fg="red", command=self.master.destroy).pack(side="bottom")


    def generate_cipher(self):

        #lists
        lows = "abcdefghijklmnopqrstuvwxyz"
        upps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        symbols = """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        allchars = lows + upps + digits + symbols

        #6 karakter 2 upps 2 digits 2 symbols
        cipher = upps[int(random()*100)%26] + upps[int(random()*100)%26]
        cipher += digits[int(random()*10)] + digits[int(random()*10)]
        cipher += symbols[int(random()*100)%33] + symbols[int(random()*100)%33]

        #6 karakter burdan bir de random 4 tane alicaz onun icin tum listeleri birlestir ve random 4 sec ve ekle
        for i in range(4):
            cipher += allchars[int(random()*100) % len(allchars)]
        
        #time to shuffle
        solution = list(cipher)
        shuffle(solution)
        solution = "".join(solution)
        
        #gen label
        tk.Label(self, text = solution).pack()
        


root = tk.Tk()
app = Application(master=root)
app.mainloop()

