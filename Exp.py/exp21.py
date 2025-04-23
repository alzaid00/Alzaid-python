#16.	Write a Python script that prompts the user to enter their phone number and email ID. It then employs Regular Expressions to verify if these inputs adhere to standard phone number and email address formats


import tkinter as tk
from tkinter import messagebox

# Function to handle the form submission
def submit_form():
    name = entry_name.get()
    branch = entry_branch.get()
    favorite_game = entry_game.get()

    if not name or not branch or not favorite_game:
        messagebox.showwarning("Input Error", "All fields must be filled!")
    else:
        # Display output as a message box
        messagebox.showinfo("Registration Successful", 
                            f"Name: {name}\nBranch: {branch}\nFavorite Game: {favorite_game}")

# Create the main window
root = tk.Tk()
root.title("College Admission Registration")

# Create and place labels and entry widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Branch:").grid(row=1, column=0, padx=10, pady=5)
entry_branch = tk.Entry(root)
entry_branch.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Favorite Game:").grid(row=2, column=0, padx=10, pady=5)
entry_game = tk.Entry(root)
entry_game.grid(row=2, column=1, padx=10, pady=5)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
