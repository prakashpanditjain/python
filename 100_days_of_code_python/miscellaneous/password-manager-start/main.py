import json
import os
import random
import string
from tkinter import Button
from tkinter import Canvas
from tkinter import END
from tkinter import Entry
from tkinter import Label
from tkinter import PhotoImage
from tkinter import Tk
from tkinter import messagebox

import pyperclip

from web_scrapping import product_name


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    """generate random password from punctuation, ascii_letter
    and digits of  length 20"""
    charset = string.digits + string.ascii_letters + string.punctuation
    rand_choice = "".join(random.choice(charset) for i in range(15))
    password_input.insert(0, rand_choice)
    pyperclip.copy(rand_choice)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    :return: Opens a file to write password for given website
    and copied it to the clipboard
    """
    website = web_input.get()
    password = password_input.get()
    email = username_input.get()
    new_data = {website:{
        'email': email,
        'password': password
        }
    }

    # check if user has given some input
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty")
        if len(website) == 0:
            web_input.focus()
        else:
            password_input.focus()

    else:
        try:
            with open('data.json',"r") as file:
                data = json.load(file)
        except:
            with open('data.json','w') as  file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)

            web_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- Button appear as pressed ------------------------------- #
def press_button():
    """
    :return: This appears button as pressed
    """
    # pass_gen_button.config(relief='sunken')
    # window.after(200,lambda: pass_gen_button.config(relief="raised"))

    # pass_gen_button.config(state='active',relief='sunken')
    # window.after(200,lambda: pass_gen_button.config(relief='raised',state='normal'))
    window.after(100, lambda: pass_gen_button.config(relief="raised", state='normal'))
    window.after(200, lambda: pass_gen_button.config(relief="sunken", state='active'))
    window.after(300, lambda: pass_gen_button.config(relief="raised", state='normal'))

# ---------------------------- Find Password ------------------------------- #
def find_password():
    user_entry = web_input.get()

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

    except Exception as e:
        messagebox.showinfo(title='File No Found',message='ERROR: FILE NOT FOUND')
    else:
        if user_entry in data:
            email = data[user_entry]['email']
            password = data[user_entry]['password']
            messagebox.showinfo(title="Website data",
                                message=f'website:  {user_entry}\n password: {password}')
        else:
            messagebox.showinfo(title='Error',message=f"No details found for {user_entry}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=80)

lock_image = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, highlightbackground=None)
canvas.create_image(100, 100, image=lock_image)
# canvas.pack()
canvas.grid(column=1, row=0)

website_label = Label(text='Website', font=('Courier'))
website_label.grid(column=0, row=1)
website_label.config()

web_input = Entry(width=21)
web_input.grid(column=1, row=1)
web_input.focus()

username_label = Label(text='Email/Username', font=('Courier'))
username_label.grid(column=0, row=2)

username_input = Entry(width=38)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, 'myemail@gmail.com')

pass_label = Label(text="Password")
pass_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

pass_gen_button = Button(text='Generate Password', relief='raised', command=generate_pass)
pass_gen_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search',font=('Courier',15),width=13,command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
