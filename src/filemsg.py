import customtkinter as ctk
from tkinter import messagebox, filedialog
import tkinter as tk
import os

#present by Vanndy

class filemsg: #class to handle file operations
    def __init__(self): #initialize
        self.input_path = "" #path to the input file
        self.msg = "" #message from the input file
    def choose_msg_from_file(self): #select a file and read the message from it
        root = ctk.CTk() #create a window
        try:
            root.withdraw() # Hide the main window
            
            self.input_path = ctk.filedialog.askopenfilename( 
            title="Select an input file",
            filetypes=(("Text files", "*.txt"), ("Config Files", "*.conf;*.json"), ("All files", "*.*"))
        ) #select a file
            root.destroy() # Close the window
            if self.input_path: #if a file is selected
                with open(self.input_path, "r") as file: #open the file
                    self.msg = file.read() #read the message
            else:
                raise ValueError("No file selected") #raise an error if no file is selected
        except Exception as e:
            return "File Not Loaded" #return an error message
            messagebox.showerror("File Error", str(e))
        else: #if no error
            return self.msg #return the message
            messagebox.showinfo("File Loaded", "Message loaded successfully!") #show a success message
    
    def get_only_path(self): #sectct path to output folder
        try:
            self.input_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=(("Text files", "*.txt"), ("Config Files", "*.conf;*.json"), ("All files", "*.*"))
            )
            if self.input_path: #if a folder is selected
                return self.input_path #return the path
            else: #if no folder is selected
                raise ValueError("No file selected, Or File Not Loaded") #raise an error
        except Exception as e: #if an error occurs
            return "File Not Loaded" #return an error message
        else: #if no error
            return self.input_path #return the path
    
    def create_file(self, text, path=""): #create a file with the provided text
        #create a file with the text provided with name as the current date and time in pm/am format
        try:
            #check if file exists
            if os.path.exists(path):
                messagebox.showwarning("File Exists", "The file already exists please wait for a second")
                raise ValueError("File Exists") #raise an error
            else: #if the file does not exist
                with open(path, "w") as file: #open the file
                    file.write(text) #write the text to the file
        except Exception as e: #if an error occurs
            messagebox.showerror("File Error", str(e)) #show an error message
        else: #if no error
            messagebox.showinfo("File", "Output saved to "+path) #show a success message



if __name__ == "__main__":
    f = filemsg()
    f.create_file("Hello World", "C:/Users/USER/Desktop")
        
