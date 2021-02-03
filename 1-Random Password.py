import tkinter

import random

frame1 = tkinter.Tk() 
def random_password():
    special_characters = [random.randint(33, 47) for i in range(2)]
    nummers = [random.randint(48, 57) for i in range(2)]          
    hoofdletters = [random.randint(65, 90) for i in range(2)]        
    kleineletters = [random.randint(97, 122) for i in range(4)]             
    generated = []

    generated.extend(special_characters)
    generated.extend(nummers)
    generated.extend(hoofdletters)
    generated.extend(kleineletters)

    password = ''                                                       
    for i in range(10):
        password += chr(generated[i])

    password_label = tkinter.Label(frame1, text=password, fg="yellow", bg="blue", font="Arial 18")
    password_label.pack(fill=tkinter.X)

def generator():
    frame = tkinter.Tk() 
    frame.title("Random Password Maker") 
    frame.geometry('600x300')
    frame.columnconfigure(0, weight=1)

    # frame_Label
    label = tkinter.Label(frame, text="The password generator is ready for you!", font=("Arial", "12", "bold"))
    label.pack()

    # acceptance_criteria_Label
    criteria_label = tkinter.Label(frame, text="""Password length must be 10 characters long. 
    It must contain at least 2 upper case letter, 2 digits and 2 special symbols.""")
    criteria_label.pack()

    # password_button
    button = tkinter.Button(frame, text="Generate a password", fg="green", font=("Arial", "12", "bold"), 
                            command=random_password)
    button.pack(padx=150, pady=50)
    frame.mainloop()    

if __name__ == '__main__': 
    generator()
