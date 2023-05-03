import math
import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# Constants
FONT_NAME = "Helvetica"


# Save Password
def submit():
    web = website.get()
    email_entry = email.get()
    pass_entry = password.get()

    if len(pass_entry) == 0 or len(email_entry) == 0 or len(web) == 0:
        messagebox.showinfo(title="LOOOOL", message="You left a field empty!!!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email_entry}\nPassword: {pass_entry}")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web} | {email_entry} | {pass_entry}\n")
                website.delete(0, END)
                password.delete(0, END)
#  random password

def generate_pswrd():
    password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4,8)
    nr_symbols = random.randint(2,8)
    nr_numbers = random.randint(2,8)

    passwordo = []
    for char in range(1, nr_letters + 1):
        passwordo += random.choice(letters)

    for char in range(1, nr_numbers + 1):
        passwordo += random.choice(numbers)

    for char in range(1, nr_symbols + 1):
        passwordo += random.choice(symbols)

    random.shuffle(passwordo)

    password_string = ""

    for char in passwordo:
        password_string += char

    password.insert(0, password_string)
    pyperclip.copy(password_string)


# UI
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

title = Label(text="#Keepin' it safe", font=(FONT_NAME, 38, "bold"))
title.grid(column=1, row=0)

website_title = Label(text="Website:")
website_title.grid(column=0, row=1)

website = Entry(width=52)
website.grid(row = 1, column=1, columnspan=2, sticky="WE", ipady=5, pady=(0,10))
website.focus()

email_title = Label(text="Email/Username:")
email_title.grid(column=0, row=2)

email = Entry(width=52)
email.grid(row=2, column=1, columnspan=2, sticky="EW",ipady=5, pady=(0,10))

password_title = Label(text="Password:")
password_title.grid(column=0, row=3, sticky="EW")

password = Entry(width=30)
password.grid(row=3, column=1, sticky="EW", pady=(0,10), ipady=5, padx=(0,10))

pass_btn = Button(text="Generate Password", command=generate_pswrd)
pass_btn.grid(row=3, column=2, sticky="we", pady=(0,10), ipady=2)

submit = Button(text="Add", width=44, command=submit)
submit.grid(row=4, column=1, columnspan=2, sticky="EW", ipady=2)

window.mainloop()
