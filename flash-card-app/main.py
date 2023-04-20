from tkinter import *
import json
import math
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
TEXT_COLOR= "#2A2F4F"
dict_words = {}
random_card = {}

# ---------------------------- READ CSV  ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    dict_words = original_data.to_dict(orient="records")
else:
    dict_words = data.to_dict(orient="records")


def pick_random_card():
    global random_card, flip_timer
    window.after_cancel(flip_timer)
    random_card = random.choice(dict_words)
    canvas.itemconfig(card_title, text="French", fill=TEXT_COLOR)
    canvas.itemconfig(card_word, text=random_card["French"], fill=TEXT_COLOR)
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)
    pass


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)
    pass

def known_card():
    dict_words.remove(random_card)
    print(f"card size: {len(dict_words)}")
    
    data = pandas.DataFrame(dict_words)
    data.to_csv("data/words_to_learn.csv", index=False)

    pick_random_card()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer  = window.after(3000, func=flip_card)

# Canvas and Image
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill=TEXT_COLOR)
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill=TEXT_COLOR)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button 
left_image = PhotoImage(file="images/wrong.png")
left_button = Button(image=left_image, highlightthickness=0, command=pick_random_card)
left_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_card)
right_button.grid(row=1, column=1)

pick_random_card()



window.mainloop()