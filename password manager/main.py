import random
from tkinter import *
from tkinter import messagebox

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letter = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    for i in input_email.get():
        if i != '@' and i not in numbers:
            letter.append(i)
        elif i in numbers:
            pass
        else:
            break
    huruf = ''
    for i in letter:
        huruf += i
    angkaSimbol = [random.choice(numbers) for i in range(random.randint(1, 4))]
    angkaSimbol.append(random.choice(symbols))
    x = ''.join(angkaSimbol)
    huruf += x
    input_pass.insert(0, huruf)
    pyperclip.copy(huruf)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(input_email.get()) == 0 or len(input_web.get()) == 0 or len(input_pass.get()) == 0:
        messagebox.showwarning(
            title='HEY!', message='DONT LEAVE ANY FIELD EMPTY')
    else:
        askuser = messagebox.askokcancel(title='Is it Ok?',
                                         message=f'{input_web.get()}\n{input_email.get()}\n{input_pass.get()}')
        if askuser:
            with open('password_generator.txt', 'a')as p:
                p.write(
                    f'{input_web.get()}|{input_email.get()}|{input_pass.get()}\n')
            input_web.delete(0, END)
            input_email.delete(0, END)
            input_pass.delete(0, END)
            input_email.insert(0, '@gmail.com')


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title('Password Manager'.title())
window.config(padx=50, pady=50)
# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
gambar = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=gambar)
canvas.grid(column=1, row=0)
# label
web_label = Label(text='Website:', font=('Open Sans', 12, 'normal'))
web_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:', font=('Open Sans', 12, 'normal'))
email_label.grid(column=0, row=2)

pass_label = Label(text='Password:', font=('Open Sans', 12, 'normal'))
pass_label.grid(column=0, row=3)
# input
input_web = Entry(width=35)
input_web.grid(row=1, column=1, columnspan=2)
input_web.focus()

input_email = Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, '@gmail.com')

input_pass = Entry(width=35)
input_pass.grid(row=3, column=1, columnspan=2)
# button
generate_button = Button(text='generate password'.title(),
                         command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add'.title(),
                         command=save, width=31)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
