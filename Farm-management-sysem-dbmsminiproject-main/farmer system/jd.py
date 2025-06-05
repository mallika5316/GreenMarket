import tkinter as tk
from tkinter import messagebox

# Function to handle the submit button click
def submit():
    username = username_entry.get()
    password = password_entry.get()
    
    valid_credentials = {
        "aiet": "aaaa",
        "cse": "bbbb",
        "mijar": "ccccc",
        "moodbidri": "1234"
    }
    
    if username in valid_credentials and valid_credentials[username] == password:
        messagebox.showinfo("Success", f"Welcome to {username}")
    else:
        messagebox.showerror("Error", "Username or password is incorrect")

# Create the main window
root = tk.Tk()
root.title("Login")

# Create and place the username label and entry
username_label = tk.Label(root, text="Username")
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the password label and entry
password_label = tk.Label(root, text="Password")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=2, columnspan=2, pady=20)

# Start the main event loop
root.mainloop()
