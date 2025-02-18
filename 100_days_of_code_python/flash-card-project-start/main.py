import random
from tkinter import Button
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Tk
from tkinter.font import ITALIC

import pandas

BACKGROUND_COLOR = "#B1DDC6"
# _______________________----------reading  french words.csv---------------------------#
to_learn = {}
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError as e:
    original_data = pandas.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card ={}


def random_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(word_text, text=current_card["French"],fill='black')
    canvas.itemconfig(title_text,text="French",fill='black')

    canvas.itemconfig(canvas_image,image=old_image)
    flip_timer = window.after(3000,flip_card)



# -----------------------change image after 3 sec----------------------------------
def flip_card():
    global current_card
    canvas.itemconfig(title_text, text='English',fill='white')
    canvas.itemconfig(word_text, text=current_card['English'] ,fill='white')
    canvas.itemconfig(canvas_image,image=new_image)

#if the word is known you will remove word from original dict and
# appned it in new dataframe in new csv file..
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    random_word()


# create window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

# create canvas
canvas = Canvas(width=800, height=540, highlightthickness=0)
old_image = PhotoImage(file='./images/card_front.png')
new_image = PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=old_image)


title_text = canvas.create_text(400, 150, text='Title', font=('Courier', 40, ITALIC), fill='black')
word_text = canvas.create_text(400, 263, text='word', font=('Courier', 60, 'bold'), fill='black')

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

cross_img = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_img, highlightthickness=0, command=random_word)
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file='images/right.png')
known_button = Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

#to get the word on very first time we will call random_word function here
random_word()


window.mainloop()