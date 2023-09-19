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
reps = 0
time = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps
    window.after_cancel(time)
    canvas.itemconfig(timer, text='00:00')
    window_label.config(text='TIMER', fg=GREEN)
    check_mark.config(text='')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def bring_to_front():
    window.lift()
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        window_label.config(text='BREAK', fg=RED)
        countdown(long_break)
        reps = 0
        bring_to_front()
    elif reps % 2 == 0:
        window_label.config(text='BREAK', fg=RED)
        countdown(short_break)
        bring_to_front()

    else:
        window_label.config(text='WORK', fg=GREEN)
        countdown(work_sec)
        bring_to_front()

#  ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(x):
    global reps
    min = math.floor(x/60)
    second = x % 60
    if min < 10:
        min = f'0{min}'
    if second < 10:
        second = f'0{second}'
    canvas.itemconfig(timer, text=f'{min}:{second}')
    if x > 0:
        global time
        time = window.after(1000, countdown, x-1)
    else:
        start_timer()
        session = math.floor(reps/2)
        marks = ''
        for i in range(session):
            marks += '✔'
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


def window_center(win):
    width = win.winfo_width()
    height = win.winfo_height()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width-width)//2
    y = (screen_height-height)//2
    win.geometry(f"{width}x{height}+{x}+{y}")


# window
window = Tk()
window.title('Pomodoro technique'.title())
window.config(padx=100, pady=50, bg=YELLOW)
window_label = Label(text='TIMER'.title(), bg=YELLOW, font=(FONT_NAME, 50, 'bold'),
                     fg=GREEN)
window_label.grid(column=1, row=1)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
gambar = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=gambar)
timer = canvas.create_text(100, 130, text='00:00', fill='white',
                           font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=2)

# button
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
reset_button = Button(text='Reset', highlightthickness=0, command=reset)
start_button.grid(column=0, row=3,)
reset_button.grid(column=4, row=3)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=4)

window.mainloop()
