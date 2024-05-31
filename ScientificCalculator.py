import tkinter as tk
from math import *

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("450x600")
root.configure(bg="#333333")

# Define the function to evaluate the expression
def evaluate_expression(event=None):
    try:
        expression = entry.get().replace('√', 'sqrt').replace('^', '**')
        # Evaluate the expression and handle trigonometric functions
        result = str(eval(expression))
        entry.delete(0, tk.END)  # Clear the entry widget
        entry.insert(tk.END, result)  # Insert the result into the entry widget
    except Exception as e:
        entry.delete(0, tk.END)  # Clear the entry widget
        entry.insert(tk.END, "Error")  # Insert "Error" if evaluation fails

# Define the function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)  # Clear the entry widget

# Define the function to append a character to the entry
def append_character(character):
    entry.insert(tk.END, character)  # Insert the character at the end of the entry widget

# Create the entry widget for input and output
entry = tk.Entry(root, font=("Arial", 24), bd=10, insertwidth=2, width=16, borderwidth=4, relief="sunken", bg="#ffffff")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=20)  # Place the entry widget

# Define button colors and font
button_bg_color = "#4d4d4d"
button_fg_color = "#ffffff"
button_active_bg_color = "#808080"
button_font = ("Arial", 18)

# Create the buttons for digits and basic operations
buttons = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'tan',
    '0', '.', '(', ')', 'log',
    '√', '^', 'ln', 'C', '='  # Added '=' to the buttons list
]

# Add buttons to the grid
row = 1
col = 0
for button in buttons:
    if button == 'C':
        # Create and place the Clear button
        tk.Button(root, text=button, padx=20, pady=20, font=button_font, bg="#ff0000", fg="#ffffff",
                  activebackground="#cc0000", relief="raised", command=clear_entry).grid(row=row, column=col, padx=5, pady=5)
    elif button == '=':
        # Create and place the Equals button
        tk.Button(root, text=button, padx=20, pady=20, font=button_font, bg="#ff8000", fg="#ffffff",
                  activebackground="#ff6600", relief="raised", command=evaluate_expression).grid(row=row, column=col, padx=5, pady=5)
    else:
        # Create and place other buttons
        tk.Button(root, text=button, padx=20, pady=20, font=button_font, bg=button_bg_color, fg=button_fg_color,
                  activebackground=button_active_bg_color, relief="raised",
                  command=lambda b=button: append_character(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 4:
        col = 0
        row += 1

# Bind the Enter key to the evaluate_expression function
root.bind('<Return>', evaluate_expression)

# Start the main loop
root.mainloop()
