# import random
# import string
# import tkinter as tk
# import pyperclip

# class PasswordGeneratorApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Password Generator")
        
#         self.label_length = tk.Label(master, text="Password Length:")
#         self.label_length.grid(row=0, column=0)
#         self.entry_length = tk.Entry(master)
#         self.entry_length.grid(row=0, column=1)
        
#         self.checkbox_letters = tk.Checkbutton(master, text="Include Letters", variable=tk.BooleanVar())
#         self.checkbox_letters.grid(row=1, column=0)
#         self.checkbox_letters.select()
        
#         self.checkbox_numbers = tk.Checkbutton(master, text="Include Numbers", variable=tk.BooleanVar())
#         self.checkbox_numbers.grid(row=1, column=1)
#         self.checkbox_numbers.select()
        
#         self.checkbox_symbols = tk.Checkbutton(master, text="Include Symbols", variable=tk.BooleanVar())
#         self.checkbox_symbols.grid(row=1, column=2)
#         self.checkbox_symbols.select()
        
#         self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
#         self.generate_button.grid(row=2, columnspan=3)
        
#         self.password_label = tk.Label(master, text="")
#         self.password_label.grid(row=3, columnspan=3)
        
#         self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
#         self.copy_button.grid(row=4, columnspan=3)
        
#     def generate_password(self):
#         try:
#             length = int(self.entry_length.get())
#             include_letters = self.checkbox_letters.var.get()
#             include_numbers = self.checkbox_numbers.var.get()
#             include_symbols = self.checkbox_symbols.var.get()
            
#             characters = ""
#             if include_letters:
#                 characters += string.ascii_letters
#             if include_numbers:
#                 characters += string.digits
#             if include_symbols:
#                 characters += string.punctuation
            
#             if not characters:
#                 self.password_label.config(text="Please select at least one character type.")
#                 return
            
#             password = ''.join(random.choice(characters) for _ in range(length))
#             self.password_label.config(text="Generated Password: " + password)
        
#         except ValueError:
#             self.password_label.config(text="Please enter a valid password length.")
    
#     def copy_to_clipboard(self):
#         password = self.password_label.cget("text")
#         password = password.replace("Generated Password: ", "")
#         pyperclip.copy(password)

# def main():
#     root = tk.Tk()
#     app = PasswordGeneratorApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()

import random
import string
import tkinter as tk
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        
        self.label_length = tk.Label(master, text="Password Length:")
        self.label_length.grid(row=0, column=0)
        self.entry_length = tk.Entry(master)
        self.entry_length.grid(row=0, column=1)
        
        self.checkbox_letters_var = tk.BooleanVar(value=True)
        self.checkbox_letters = tk.Checkbutton(master, text="Include Letters", variable=self.checkbox_letters_var)
        self.checkbox_letters.grid(row=1, column=0)
        
        self.checkbox_numbers_var = tk.BooleanVar(value=True)
        self.checkbox_numbers = tk.Checkbutton(master, text="Include Numbers", variable=self.checkbox_numbers_var)
        self.checkbox_numbers.grid(row=1, column=1)
        
        self.checkbox_symbols_var = tk.BooleanVar(value=True)
        self.checkbox_symbols = tk.Checkbutton(master, text="Include Symbols", variable=self.checkbox_symbols_var)
        self.checkbox_symbols.grid(row=1, column=2)
        
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, columnspan=3)
        
        self.password_label = tk.Label(master, text="")
        self.password_label.grid(row=3, columnspan=3)
        
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=4, columnspan=3)
        
    def generate_password(self):
        try:
            length = int(self.entry_length.get())
            include_letters = self.checkbox_letters_var.get()
            include_numbers = self.checkbox_numbers_var.get()
            include_symbols = self.checkbox_symbols_var.get()
            
            characters = ""
            if include_letters:
                characters += string.ascii_letters
            if include_numbers:
                characters += string.digits
            if include_symbols:
                characters += string.punctuation
            
            if not characters:
                self.password_label.config(text="Please select at least one character type.")
                return
            
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text="Generated Password: " + password)
        
        except ValueError:
            self.password_label.config(text="Please enter a valid password length.")
    
    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        password = password.replace("Generated Password: ", "")
        pyperclip.copy(password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
