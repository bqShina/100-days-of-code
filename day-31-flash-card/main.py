from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}

# read data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_data = original_data.to_dict(orient="records")
else:
    word_data = data.to_dict(orient="records")


def random_french():
    global random_word, flip
    window.after_cancel(flip)
    random_word = random.choice(word_data)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    canvas.itemconfig(card, image=card_front_image)
    flip = window.after(3000, func=card_flip)


def card_flip():
    global random_word
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=random_word["English"], fill="white")


def remove_word():

    global random_word
    word_data.remove(random_word)
    to_learn = pandas.DataFrame(word_data)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    random_french()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip = window.after(3000, func=card_flip)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_image)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
button_right = Button(image=right_image, highlightthickness=0, command=remove_word)
button_wrong = Button(image=wrong_image, highlightthickness=0, command=random_french)
button_right.grid(column=1, row=1)
button_wrong.grid(column=0, row=1)

random_french()


window.mainloop()
