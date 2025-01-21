import tkinter as tk
from tkinter import messagebox, simpledialog
import pyperclip

class ButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Button App")
        
        self.button_texts = ["Button 1", "Button 2", "Button 3"]
        self.buttons = []
        
        self.create_buttons()
        self.create_input_box()
        self.create_settings_button()
    
    def create_buttons(self):
        for i, text in enumerate(self.button_texts):
            button = tk.Button(self.root, text=text, command=lambda t=text: self.copy_to_clipboard(t))
            button.grid(row=i, column=0, padx=10, pady=5)
            self.buttons.append(button)
    
    def create_input_box(self):
        self.input_var = tk.StringVar()
        self.input_box = tk.Entry(self.root, textvariable=self.input_var, width=50)
        self.input_box.grid(row=len(self.button_texts), column=0, padx=10, pady=10)
        self.paste_button = tk.Button(self.root, text="Paste from Clipboard", command=self.paste_from_clipboard)
        self.paste_button.grid(row=len(self.button_texts) + 1, column=0, padx=10, pady=5)
    
    def create_settings_button(self):
        self.settings_button = tk.Button(self.root, text="Settings", command=self.open_settings)
        self.settings_button.grid(row=len(self.button_texts) + 2, column=0, padx=10, pady=5)
    
    def copy_to_clipboard(self, text):
        pyperclip.copy(text)
        messagebox.showinfo("Info", f"Copied '{text}' to clipboard")
    
    def paste_from_clipboard(self):
        text = pyperclip.paste()
        self.input_var.set(text)
        messagebox.showinfo("Info", f"Pasted '{text}' from clipboard")
    
    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Button Settings")
        
        self.settings_window = settings_window
        self.settings_entries = []
        
        for i, text in enumerate(self.button_texts):
            label = tk.Label(settings_window, text=f"Button {i+1} Text:")
            label.grid(row=i, column=0, padx=10, pady=5)
            
            entry = tk.Entry(settings_window, width=30)
            entry.insert(0, text)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.settings_entries.append(entry)
        
        save_button = tk.Button(settings_window, text="Save", command=self.save_settings)
        save_button.grid(row=len(self.button_texts), column=0, columnspan=2, pady=10)
    
    def save_settings(self):
        new_texts = [entry.get() for entry in self.settings_entries]
        self.button_texts = new_texts
        
        for i, button in enumerate(self.buttons):
            button.config(text=new_texts[i])
        
        self.settings_window.destroy()
        messagebox.showinfo("Info", "Settings saved successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = ButtonApp(root)
    root.mainloop()