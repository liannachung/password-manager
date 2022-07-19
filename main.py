from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = username_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def search_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="No data file found")
    else:
        website_name = website_entry.get()
        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showinfo(message=f"No details for {website_name} exist")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 20, "normal"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=19)
website_entry.focus()
website_entry.grid(column=1, row=1)
search_button = Button(text="Search", width=10, command=search_password)
search_button.grid(column=2, row=1)

username_label = Label(text="Email/Username:", font=("Arial", 20, "normal"))
username_label.grid(column=0, row=2)
username_entry = Entry(width=35)
username_entry.insert(0, "liannachungg@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", font=("Arial", 20, "normal"))
password_label.grid(column=0, row=3)
password_entry = Entry(width=19)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save_password, width=34)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()