from tkinter import *
import pandas
import time
import random

# ------------- Constants -----------------#
BG_COLOR = "#B1DDC6"

data = pandas.read_csv("data.csv")
to_learn = data.to_dict(orient="records")
current = {}


# ------------- Methods -----------------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Italien", fill="black")
    canvas.itemconfig(card_word, text=current_card["Italiano"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(4000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="Français", fill="white")
    canvas.itemconfig(card_word, text=current_card["Francais"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def got_it_right():
    to_learn.remove(current_card)
    next_card()


# ------------- UI -----------------#
window = Tk()
window.title("Io parlo italiano (con errori)")
window.config(padx=100, pady=100, bg=BG_COLOR)

flip_timer = window.after(4000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 158, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 68, "bold"))

canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
cross_img = PhotoImage(file="images/wrong.png")
dontknow_btn = Button(image=cross_img, command=next_card)
dontknow_btn.config(highlightthickness=0)
dontknow_btn.grid(row=1, column=0)

checkmark_img = PhotoImage(file="images/right.png")
know_btn = Button(image=checkmark_img, command=got_it_right)
know_btn.config(highlightthickness=0)
know_btn.grid(row=1, column=1)

next_card()

window.mainloop()
