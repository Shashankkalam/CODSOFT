import tkinter as tk
from tkinter import StringVar
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.password_var = StringVar()
        self.password_var.set("")

        # Entry widget to display the generated password
        self.password_entry = tk.Entry(master, textvariable=self.password_var, font=('Arial', 14), bd=10, insertwidth=4, width=20, justify='center')
        self.password_entry.grid(row=0, column=0, columnspan=3, pady=10)

        # Button to generate a new password
        tk.Button(master, text="Generate Password", command=self.generate_password, width=20, height=2).grid(row=1, column=0, columnspan=3, pady=10)

        # Button to copy the password to the clipboard
        tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard, width=20, height=2).grid(row=2, column=0, columnspan=3, pady=10)

    def generate_password(self):
        length = 12  # You can customize the length of the password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            self.master.update()
            tk.messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            tk.messagebox.showwarning("Warning", "Generate a password first.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
