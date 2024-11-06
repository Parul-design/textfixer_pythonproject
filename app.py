import tkinter as tk
from tkinter import Label, Entry, Button
from textblob import TextBlob

# Create the main window
root = tk.Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

# Function to check spelling
def check_spelling():
    word = enter_text.get()  # Get the input text
    a = TextBlob(word)       # Create a TextBlob object
    corrected = str(a.correct())  # Get the corrected text
    spell.config(text=corrected)  # Update the label with corrected text

# Heading label
heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))

# Entry widget for text input
enter_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

# Button to check spelling
button = Button(root, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
button.pack()

# Label to display corrected text
spell = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spell.place(x=100, y=250)

# Run the application
root.mainloop()
