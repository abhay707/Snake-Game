import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv('data/french_words.csv')
# french_words = []
# new_dict = {row.French: row.English for (index, row) in data.iterrows()}
# french_words.append(new_dict)
to_learn = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 265, text="", font=("Ariel", 60, "bold"))

cancel_image = PhotoImage(file='E:/codes/Python/projects/flash card project/images/wrong.png')
button_cancel = Button(image=cancel_image, highlightthickness=0, command=next_card)
button_cancel.grid(column=0, row=1)

right_image = PhotoImage(file='E:/codes/Python/projects/flash card project/images/right.png')
button_right = Button(image=right_image, highlightthickness=0, command=next_card)
button_right.grid(column=1, row=1)

next_card()








window.mainloop()