from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    #Password Generator Project 2.0 (With list comprehension)
    from random import randint, choice, shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
Number = 0

def save():

    global website
    global email
    global password
    global Number
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty.")
    else:
        Number += 1
        save_pass()

def save_pass():
    is_ok = messagebox.askokcancel(title=website,
                                   message=f"These are the details entered:\n Email: {email} "f"\n Password: {password} \n Is it ok to save?")
    if is_ok:
        with open(file="data.txt", mode="a") as passwords:
            passwords.write(f"\n{Number}. {website} | {email} | {password}")
            passwords.close()
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=50, padx=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)

# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Entries
website_entry = Entry(width=38)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.insert(0, "anirudhbalaji06@gmail.com")
password_entry = Entry()

# Buttons
generate_pass_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=38, command=save)

# Grid Layout
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_label.config(justify="left")
email_label.grid(row=2, column=0)
email_label.config(justify="left")
password_label.grid(row=3, column=0)
password_label.config(justify="left")

website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry.grid(row=3, column=1, sticky="EW")

generate_pass_button.grid(row=3, column=2, sticky="EW")
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

website_label.grid(row=1, column=0)

window.mainloop()
