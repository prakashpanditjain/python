from tkinter import PhotoImage, Canvas, Tk, Label, Entry, Button


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from django.forms.widgets import Input

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #



# ---------------------------- Button appear as pressed ------------------------------- #
def press_button():
    # pass_gen_button.config(relief='sunken')
    # window.after(200,lambda: pass_gen_button.config(relief="raised"))

    pass_gen_button.config(state='active')
    window.after(200,lambda: pass_gen_button.config(state='normal'))




window = Tk()
window.title("Password Manager")
window.config(padx=100,pady=50)

lock_image = PhotoImage(file='logo.png')
canvas = Canvas(width=200,height=200,highlightbackground='white')
canvas.create_image(100,100,image=lock_image)
# canvas.pack()
canvas.grid(column=1,row=0)

website_label = Label(text='Website',font=('Courier'))
website_label.grid(column=0,row=1)

web_input = Entry(width=35,bg='white')
web_input.grid(column=1,row=1,columnspan=2)

username_label = Label(text='Email/Username',font=('Courier'))
username_label.grid(column=0,row=2)

username_input = Entry(width=35,bg='white')
username_input.grid(column=1,row=2,columnspan=2)

pass_label = Label(text="Password")
pass_label.grid(column=0,row=3)

password_input = Entry(width=21,bg='white')
password_input.grid(column=1,row=3)

pass_gen_button = Button(window, text='Generate Password',fg='green',command=press_button)
pass_gen_button.grid(column=2,row=3)




window.mainloop()