import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text='00:00')
    timer_label.config(text='Timer')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # count_down(5*60)

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_Sec = LONG_BREAK_MIN * 60

    if reps in (1,3,5,7):
        count_down(work_sec)
        timer_label.config(text='WORK TIMER',fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='SHORT BREAK',fg=YELLOW)
    elif reps % 8 == 0:
        count_down(long_break_Sec)
        timer_label.config(text="LONG BREAK",fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor( count / 60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count-1)
        print(count)
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(reps/2)):
            marks += '✅'
        check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=PINK)

# def say_something(a,b,c):
#     print('thing')
#     print(a,b,c)
#
# window.after(1000,say_something,3,45,6)


canvas = Canvas(width=200,height=225,bg=PINK,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)
# count_down(5)

timer_label = Label(text='Timer',font=('Courier',50,'bold'),bg=PINK)
timer_label.grid(column=1,row=0)


start_button = Button(text='Start',font=('Courier',20,'bold'),bg=PINK,highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset',font=('Courier',20,'bold'),bg=PINK,highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks = Label(text='',bg=PINK)
check_marks.grid(column=1,row=3)



window.mainloop()