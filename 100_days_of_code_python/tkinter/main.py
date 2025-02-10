import random
import tkinter

from click import clear

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=400,height=400)

my_lable = tkinter.Label(text='I am a Lable',font=('Courier',20,"bold"))
my_lable.pack(side= 'top')

def button_clicked():
    new_text= input.get()
    my_lable.config(text=new_text)
    # my_lable.pack(side='bottom')

position =['right','left','top','bottom']

button = tkinter.Button(text='Click Me',command=button_clicked)
button.pack()

input = tkinter.Entry()
input.pack()

window.mainloop()