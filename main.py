import customtkinter as ctk
from tkinter import messagebox
from encrypt import encrypt
from decrypt import decrypt
from PIL import Image
from filemsg import filemsg
from asset.mydailog import CustomDialog

# Initialize Encrypt and Decrypt objects
e = encrypt()
d = decrypt()
f = filemsg()
OUTPUT_FILE = "output.txt"
LOGO = "projectpy/image/logo.png"
LOGO1 = "image/logo.png"

# Function to handle encryption and decryption
def perform_action(input_field, output_field, password_field, action_var, out_var,op_path=""):
    message = input_field.get("1.0", "end-1c").strip() # 1.0 is the start of the text and end-1c is the end of the text without the last character (newline) 
    password = password_field.get().strip() # Remove leading and trailing whitespaces
    if not message or not password:
        messagebox.showwarning("Input Error", "Both message and password are required!")
        return

    action = action_var.get()
    out_type = out_var.get()
    try:
        if out_type == "File":
            if op_path == "":
                raise ValueError("No output path selected")
            messagebox.showinfo("File", "Output saved to "+op_path)
        elif out_type == "none":
            pass
    except Exception as err:
        messagebox.showerror("Action Error", str(err))
      
    try:
        if action == "Encrypt":
            result = e.encrypt(message, password) # Encrypt the message
        elif action == "Decrypt":
            result = d.decrypt(message, password) # Decrypt the message
        else:
            raise ValueError("Invalid action selected")

        output_field.delete("1.0", "end")
        output_field.insert("1.0", result) # 1.0 is the start of the text
    except Exception as err:
        messagebox.showerror("Action Error", str(err))


def copy_to_clipboard(text):
    root = ctk.CTk()
    root.withdraw() # Hide the main window
    root.clipboard_clear() # Clear the clipboard
    root.clipboard_append(text) # Append the text to the clipboard
    root.update() # Update the clipboard
    root.destroy() # Close the window
    messagebox.showinfo("Copied", "Output copied to clipboard!")

def insert_text_to_input(input_field):
    text = f.choose_msg_from_file()
    print(text)
    input_field.delete("1.0", "end") # 1.0 is the start of the text and end is the end of the text
    input_field.insert("1.0", text)
    messagebox.showinfo("Text Loaded", "Text loaded successfully!")
def get_path_and_insert_text_to_input(input_field):
    text = f.get_only_path()
    input_field.delete("1.0", "end") # 1.0 is the start of the text and end is the end of the text
    input_field.insert("1.0", text)
    

# Main application function
def create_app():
    # Configure the appearance of customtkinter
    def switch_event():
        if switch_var.get() == "off":
            ctk.set_appearance_mode("Dark")  # Modes: "Dark", "Light"
        else:       
            ctk.set_appearance_mode("Light")

    ctk.set_default_color_theme("green")  # Themes: "blue", "green", "dark-blue"
    app = ctk.CTk()

    app.title("SAR SOM NGAT") # Set the title of the window
    app.geometry("900x750")
    #set the icon
    
    
    try:
        app.iconbitmap("projectpy/image/logo.ico")
    except:
        app.iconbitmap("image/logo.ico")
    


    # Header
    header_frame = ctk.CTkFrame(app, corner_radius=15)
    header_frame.pack(pady=10, padx=20, fill="x")

    # Load the logo image
    try:
        logo_image = ctk.CTkImage(Image.open(LOGO1), size=(100, 100))  # Adjust size as needed
    except:
        logo_image = ctk.CTkImage(Image.open(LOGO), size=(100, 100))
    # Add the logo image to a label
    logo_label = ctk.CTkLabel(header_frame, image=logo_image, text="", width=100, height=100)
    logo_label.pack( padx=10)

    # Add the title text next to the logo
    title_label = ctk.CTkLabel(header_frame, text="SAR SOM NGAT", font=("Helvetica", 40, "bold"))
    title_label.pack(padx=10)

    # Switch colors
    switch_var = ctk.StringVar(value="off")
    switch = ctk.CTkSwitch(header_frame, text="Dark/Light", font=("Helvetica", 16), command=switch_event,variable=switch_var, onvalue="on", offvalue="off")
    switch.pack(pady=10, padx=20,side="right")
    # Input Section
    input_frame = ctk.CTkFrame(app, corner_radius=15)
    input_frame.pack(pady=10, padx=20, fill="x")

    message_label = ctk.CTkLabel(input_frame, text="Message:", font=("Helvetica", 14))
    message_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    input_text = ctk.CTkTextbox(input_frame, height=70, font=("Helvetica", 16))
    input_text.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    choose_file = ctk.CTkButton(input_frame, text="Choose File",font=("romnea",13), command=lambda: insert_text_to_input(input_text))
    choose_file.grid(row=0, column=2, padx=10)

    password_label = ctk.CTkLabel(input_frame, text="Password:", font=("Helvetica", 14))
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    password_entry = ctk.CTkEntry(input_frame, font=("Helvetica", 16))
    password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    input_frame.grid_columnconfigure(1, weight=1)

    # Action Selection  
    action_frame = ctk.CTkFrame(app, corner_radius=15)
    action_frame.pack(pady=5, padx=20, fill="x")

    action_var = ctk.StringVar(value="Encrypt")
    action_label = ctk.CTkLabel(action_frame, text="Select Action:", font=("Helvetica", 14))
    action_label.pack(side="left", padx=10)
    encrypt_radio = ctk.CTkRadioButton(action_frame, text="Encrypt", variable=action_var, value="Encrypt")
    encrypt_radio.pack(side="left", padx=10)
    decrypt_radio = ctk.CTkRadioButton(action_frame, text="Decrypt", variable=action_var, value="Decrypt")
    decrypt_radio.pack(side="left", padx=10)

     # Function Choose location to store the output
    def choose_location():
        if out_var.get() == "none":
            choose_location.pack_forget()
            output_frame1.pack_forget()
            action_button1.pack_forget()
            output_frame1.pack(pady=5, padx=20, fill="x")
            action_button1.pack(pady=15)

        elif out_var.get() == "File":
            output_frame1.pack_forget()
            action_button1.pack_forget()
            choose_location.pack(pady=10, padx=20, fill="x")
            output_frame1.pack(pady=5, padx=20, fill="x")
            action_button1.pack(pady=5)

    # Output Selection
    OP_frame = ctk.CTkFrame(action_frame, corner_radius=0, fg_color="transparent")
    OP_frame.pack(padx=5, fill="x")
    out_var = ctk.StringVar(value="none")
    file_radio = ctk.CTkRadioButton(OP_frame, text="File", command=choose_location, variable=out_var, value="File", )
    file_radio.pack(side="right", padx=10)
    none_radio = ctk.CTkRadioButton(OP_frame, text="None", command=choose_location, variable=out_var, value="none", fg_color="red")
    none_radio.pack(side="right", padx=10)
    action_label = ctk.CTkLabel(OP_frame, text="Select Output:", font=("Helvetica", 14))
    action_label.pack(side="right", padx=10)
    
    # choose location store results 
    choose_location = ctk.CTkFrame(app, corner_radius=15)
    message_label2 = ctk.CTkLabel(choose_location, text="Store Results In:", font=("Helvetica", 14))
    message_label2.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    input_text2 = ctk.CTkTextbox(choose_location, font=("Helvetica", 13), height=1)
    input_text2.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    choose_file2 = ctk.CTkButton(choose_location, text="Choose Path",font=("romnea",13), command=lambda: get_path_and_insert_text_to_input(input_text2))
    choose_file2.grid(row=0, column=2, padx=10, sticky="w")
    choose_location.grid_columnconfigure(1, weight=1)  

    # Output Results  
    output_frame1 = ctk.CTkFrame(app, corner_radius=15)
    output_frame1.pack(pady=5, padx=20, fill="x")

    output_label = ctk.CTkLabel(output_frame1, text="Results:", font=("Helvetica", 14))
    output_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    output_text = ctk.CTkTextbox(output_frame1, height=70, font=("Helvetica", 16))
    output_text.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    copy_button = ctk.CTkButton(output_frame1, text="Copy",font=("romnea",13), command=lambda: copy_to_clipboard(output_text.get("1.0", "end-1c"))) # 1.0 is the start of the text and end-1c is the end of the text
    copy_button.grid(row=0, column=2, padx=10)

    output_frame1.grid_columnconfigure(1, weight=1)

    # Perform Action Button
    action_button1 = ctk.CTkButton(app, text="Start", font=("romnea", 14), command=lambda: perform_action(input_text, output_text, password_entry, action_var, out_var,input_text2.get("1.0", "end-1c")))
    action_button1.pack(pady=15)

    app.mainloop()


if __name__ == "__main__":
    create_app()
