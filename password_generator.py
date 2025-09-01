
from tkinter import *

window = Tk()
window.title("Password Generator")
window.geometry("400x400")
window.iconbitmap("./assets/logo.ico")
window.configure(bg="#282A36")

# Image creation
img_width = 300
img_height = 300
img = PhotoImage(file="./assets/password.png").zoom(10).subsample(32)
canvas = Canvas(window, width=img_width, height=img_height, bg=window.cget("bg"), highlightthickness=0)
canvas.create_image(img_width // 2, img_height // 2, image=img)
canvas.pack(expand=True)

# Password Entry
password_var = StringVar()
password_entry = Entry(window, textvariable=password_var, font=("Arial", 16), width=22, justify="center")
password_entry.pack(pady=10)

import random
import string

def generate_password():
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_var.get())

def clear_fields():
    password_var.set("")

# Buttons
btn_frame = Frame(window, bg=window.cget("bg"))
btn_frame.pack(pady=10)

generate_btn = Button(btn_frame, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#6272A4", fg="white", relief=RAISED)
generate_btn.grid(row=0, column=0, padx=5)

copy_btn = Button(btn_frame, text="Copy", command=copy_to_clipboard, font=("Arial", 12), bg="#50FA7B", fg="black", relief=RAISED)
copy_btn.grid(row=0, column=1, padx=5)

clear_btn = Button(btn_frame, text="Clear", command=clear_fields, font=("Arial", 12), bg="#FF5555", fg="white", relief=RAISED)
clear_btn.grid(row=0, column=2, padx=5)

window.mainloop()
