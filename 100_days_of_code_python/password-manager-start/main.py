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

    def delete_entries():
        """
        :return: deletes the entries from Entry box of website and password
        """
        web_input.delete(0, END)
        password_input.delete(0, END)

    def write_content():
        """
        :return: website , username and password
        """
        content = (f'{website} \t|\t {email} \t|\t {password}\n')
        return content

    # check if user has given some input
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty")
        if len(website) == 0:
            web_input.focus()
        else:
            password_input.focus()

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Website: {website}\n Password: {password}\n Are your entries are "
                                               f"confirm to add")
        # check if file path do exists
        file_path = os.path.exists('data.txt')
        if is_ok:
            if file_path is False:
                with open('../password-manager-start/data.txt', 'w') as file:
                    # write the header in the file for first time
                    file.write("website \t|\t Username\t|\t Password\n")

            with open('../password-manager-start/data.txt', 'a') as file:
                    file.write(write_content())
                    delete_entries()
        else:
            web_input.focus()


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

web_input = Entry(width=38, )
web_input.grid(column=1, row=1, columnspan=2)
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

window.mainloop()
