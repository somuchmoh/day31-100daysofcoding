import tkinter
from tkinter import PhotoImage
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
current_card = {}

# -------------------------- RANDOMISATION OF CARDS AND FLIPPING -------------------------- #
try:
    data = pandas.read_csv('Data/words_to_learn.csv')
except FileNotFoundError:
    og_data = pandas.read_csv('Data/Python_Flashcards - Spanish.csv')
    data_dict = og_data.to_dict(orient='records')
else:
    # Convert the DataFrame to a Dictionary
    data_dict = data.to_dict(orient='records')


def pick_word():
    global current_card, timer
    window.after_cancel(id=timer)
    current_card = random.choice(data_dict)
    print(current_card)
    canvas.itemconfig(card_title, text="Spanish", fill='Black')
    canvas.itemconfig(card_word, text=current_card['Spanish'], fill='Black')
    canvas.itemconfig(card_image, image=card_front)
    timer = window.after(3000, func=show_translation)


def show_translation():
    canvas.itemconfig(card_title, text="English", fill='White')
    canvas.itemconfig(card_word, text=current_card['English'], fill='White')
    canvas.itemconfig(card_image, image=card_back)


# -------------------------- UPDATE LIST WITH KNOWN WORDS -------------------------- #


def remove_word():
    data_dict.remove(current_card)
    pick_word()
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv('Data/words_to_learn.csv', index=False)

# -------------------------- UI SETUP -------------------------- #


window = tkinter.Tk()
window.config(bg=BACKGROUND_COLOR, width=800, height=800, padx=50, pady=50)
window.title("Flash Cards")
timer = window.after(3000, func=show_translation)

# Canvas for Flash Cards
canvas = tkinter.Canvas()
canvas.config(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=2)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 265, image=card_front)
card_title = canvas.create_text(400, 150, text="Language", fill="black", font=("Ariel", 40, 'italic'))
card_word = canvas.create_text(400, 300, text='Word', fill="black", font=("Ariel", 60, 'bold'))

# Wrong Button
cross_image = PhotoImage(file="images/wrong.png")
cross = tkinter.Button(image=cross_image, highlightthickness=0, borderwidth=0, command=pick_word)
cross.grid(row=2, column=1)

# Right Button
tick_image = PhotoImage(file="images/right.png")
tick = tkinter.Button(image=tick_image, highlightthickness=0, borderwidth=0, command=remove_word)
tick.grid(row=2, column=2)

window.mainloop()
