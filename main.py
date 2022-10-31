import pyperclip
from tkinter import *
from tkinter import messagebox
from generator import Generate


gen_pass = Generate()

website_empty = ""
email_empty = ""
password_empty = ""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    entry_password.delete(0, END)
    gen_pass.generate()
    entry_password.insert(0, gen_pass.password)
    pyperclip.copy(gen_pass.password)
    pyperclip.paste()
    gen_pass.clear()
# ---------------------------- SAVE PASSWORD ------------------------------- #


def check_empty(user_website, user_email, user_password):
    global website_empty, email_empty, password_empty
    if user_website == "":
        website_empty = True
    if user_email == "":
        email_empty = True
    if user_password == "":
        password_empty = True


def save_info():
    global website_empty, email_empty, password_empty
    user_website = entry_website.get()
    user_email = entry_email.get()
    user_password = entry_password.get()

    check_empty(user_website, user_email, user_password)

    if website_empty is True or email_empty is True or password_empty is True:
        messagebox.showerror(title="Invalid Inputs", message=f"Fields cannot be empty")
        website_empty = False
        email_empty = False
        password_empty = False
    else:
        is_ok = messagebox.askokcancel(title=user_website, message=f"These are the details entered?\n"
                                                                   f"Email: {user_email}"
                                                                   f" and Password: {user_password}")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{user_website} | {user_email} | {user_password}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50, bg="lightblue")
window.title("Password Hero")

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="lightblue", highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


label_website = Label(text="Website", bg="lightblue", foreground="#121212")
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username", bg="lightblue", foreground="#121212")
label_email.grid(column=0, row=2)
label_password = Label(text="Password", bg="lightblue", foreground="#121212")
label_password.grid(column=0, row=3)


entry_website = Entry(width=35)
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2)
entry_email = Entry(width=35)
entry_email.insert(0, "dilipbadal@gmail.com")
entry_email.grid(column=1, row=2, columnspan=2)
entry_password = Entry(width=17)
entry_password.grid(column=1, row=3)

button_generate = Button(text="Generate Password", width=14, command=generate)
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", width=36, padx=10, command=save_info)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()
