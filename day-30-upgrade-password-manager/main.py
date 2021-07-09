from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for _ in range(nr_letters)] + [choice(symbols) for _ in range(nr_symbols)]\
                     + [choice(numbers) for _ in range(nr_numbers)]

    shuffle(password_list)
    new_password = ''.join(password_list)
    password_input.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_input.get()
    email_username_data = email_username_input.get()
    password_data = password_input.get()
    new_data = {
        website_data: {
            "email": email_username_data,
            "password": password_data,
        }
    }
    if len(website_data) == 0 or len(email_username_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- Find Password ------------------------------- #
def find_password():
    website_data = website_input.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File Found.")
    else:
        print("works")
        if website_data in data:
            messagebox.showinfo(title=website_data, message=f"Email: {data[website_data]['email']}\n"
                                                            f"Password: {data[website_data]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"There is no details of {website_data} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# entry
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "bqshina@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# button
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)
generate_password = Button(text="Generate Password", command=password_generate)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
