import customtkinter as ctk
from tkinter import messagebox


class filemsg:
    def __init__(self):
        self.input_path = ""
        self.msg = ""
    def choose_msg_from_file(self):
        root = ctk.CTk()
        try:
            root.withdraw() # Hide the main window
            self.input_path = ctk.filedialog.askopenfilename(
            title="Select an input file",
            filetypes=(("Text files", "*.txt"), ("Config Files", "*.conf;*.json"), ("All files", "*.*"))
        )
            root.destroy() # Close the window
            if self.input_path:
                with open(self.input_path, "r") as file:
                    self.msg = file.read()
            else:
                raise ValueError("No file selected")
        except Exception as e:
            return "File Not Loaded"
            messagebox.showerror("File Error", str(e))
        else:
            return self.msg
            messagebox.showinfo("File Loaded", "Message loaded successfully!")
    def get_only_path(self): #sectct path to output folder

        root = ctk.CTk()
        try:
            self.input_path = ctk.filedialog.askdirectory()
            root.destroy() # Close the window
            if self.input_path:
                return self.input_path
            else:
                raise ValueError("No file selected, Or File Not Loaded")
        except Exception as e:
            return "File Not Loaded"
        else:
            return self.input_path
        
