import string
import random
from typing import Union
import customtkinter as ctk
import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("green")

def generate_password():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_special_characters = special_var.get()

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    special_characters = string.punctuation if include_special_characters else ""

    password_characters = lowercase_letters + uppercase_letters + numbers + special_characters

    password = ''.join(random.choice(password_characters) for _ in range(length))
    password_var.set(password)

    # Determine the strength of the password based on its length and character set
    if length < 8 or len(password_characters) < 4:
        strength = "Weak"
        color = "#FF0000"  # Red
    elif length < 12 or len(password_characters) < 6:
        strength = "Medium"
        color = "#FFA500"  # Orange
    else:
        strength = "Strong"
        color = "#008000"  # Green

    # Set the text and color of the strength label
    strength_var.set(strength)
    strength_label.configure(text_color=color)

# Create the main window
window = ctk.CTk()
window.geometry("400x500")
window.title("Random Password Generator")

# Create a label for the length field
length_label = ctk.CTkLabel(window, text="Password length:",font=("Arial", 30))
length_label.pack(padx=10, pady=10)

# Create an entry field for the length
length_var = ctk.StringVar(value="8")
length_entry = ctk.CTkEntry(window, textvariable=length_var,font=("Arial", 16),width=50,justify="center")
length_entry.pack(padx=10, pady=10)

# Create checkboxes for uppercase letters, numbers, and special characters
uppercase_var = ctk.BooleanVar()
uppercase_checkbutton = ctk.CTkCheckBox(window, text="Include uppercase letters",font=("Arial", 18), variable=uppercase_var)
uppercase_checkbutton.pack(pady=10)

numbers_var = ctk.BooleanVar()
numbers_checkbutton = ctk.CTkCheckBox(window, text="Include numbers", font=("Arial", 18),variable=numbers_var)
numbers_checkbutton.pack(pady=10)

special_var = ctk.BooleanVar()
special_checkbutton = ctk.CTkCheckBox(window, text="Include special characters",font=("Arial", 18), variable=special_var)
special_checkbutton.pack(pady=10)


# Create a button to generate the password
generate_button = ctk.CTkButton(window, text="Generate password",font=("Arial", 18), command=generate_password,width=50)
generate_button.pack(padx=10, pady=10)

# Create a label to display the generated password


password_var = ctk.StringVar()
password_label = ctk.CTkLabel(window, textvariable=password_var, font=("Arial", 25),justify="center")
password_label.pack(padx=10, pady=10)

# Create a label to display the strength of the password
strength_var = ctk.StringVar(value="")

strength_label = ctk.CTkLabel(window, textvariable=strength_var, font=("Arial", 25),justify="center")
strength_label.pack(padx=10, pady=10)

# Start the main loop
window.geometry("400x450")
window.mainloop()
