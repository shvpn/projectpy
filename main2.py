import customtkinter as ctk
from tkinter import messagebox
from encrypt import encrypt
from decrypt import decrypt
from PIL import Image

# Initialize Encrypt and Decrypt objects
e = encrypt()
d = decrypt()


# Function to handle encryption and decryption
def perform_action(input_field, output_field, password_field, action_var):
    message = input_field.get("1.0", "end-1c").strip()
    password = password_field.get().strip()
    if not message or not password:
        messagebox.showwarning("Input Error", "Both message and password are required!")
        return

    action = action_var.get()
    try:
        if action == "Encrypt":
            result = e.encrypt(message, password)
        elif action == "Decrypt":
            result = d.decrypt(message, password)
        else:
            raise ValueError("Invalid action selected")

        output_field.delete("1.0", "end")
        output_field.insert("1.0", result)
    except Exception as err:
        messagebox.showerror("Action Error", str(err))


def copy_to_clipboard(text):
    root = ctk.CTk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    root.destroy()
    messagebox.showinfo("Copied", "Output copied to clipboard!")


# Main application function
def create_app():
    # Configure the appearance of customtkinter
    ctk.set_appearance_mode("Dark")  # Modes: "Dark", "Light"
    ctk.set_default_color_theme("green")  # Themes: "blue", "green", "dark-blue"

    app = ctk.CTk()
    app.title("Encryption/Decryption App")
    app.geometry("900x600")

    # Header
    header_frame = ctk.CTkFrame(app, corner_radius=15)
    header_frame.pack(pady=20, padx=20, fill="x")

    # Load the logo image
    logo_image = ctk.CTkImage(Image.open("ok6.png"), size=(100, 100))  # Adjust size as needed

    # Add the logo image to a label
    logo_label = ctk.CTkLabel(header_frame, image=logo_image, text="", width=100, height=100)
    logo_label.pack( padx=10)

    # Add the title text next to the logo
    title_label = ctk.CTkLabel(header_frame, text="SSNG", font=("Helvetica", 40, "bold"))
    title_label.pack(padx=10)
    # Input Section
    input_frame = ctk.CTkFrame(app, corner_radius=15)
    input_frame.pack(pady=20, padx=20, fill="x")

    message_label = ctk.CTkLabel(input_frame, text="Message:", font=("Helvetica", 14))
    message_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    input_text = ctk.CTkTextbox(input_frame, height=70, font=("Helvetica", 12))
    input_text.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    password_label = ctk.CTkLabel(input_frame, text="Password:", font=("Helvetica", 14))
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    password_entry = ctk.CTkEntry(input_frame, font=("Helvetica", 12))
    password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    input_frame.grid_columnconfigure(1, weight=1)

    # Action Selection
    action_frame = ctk.CTkFrame(app, corner_radius=15)
    action_frame.pack(pady=10, padx=20, fill="x")

    action_var = ctk.StringVar(value="Encrypt")
    action_label = ctk.CTkLabel(action_frame, text="Select Action:", font=("Helvetica", 14))
    action_label.pack(side="left", padx=10)
    encrypt_radio = ctk.CTkRadioButton(action_frame, text="Encrypt", variable=action_var, value="Encrypt")
    encrypt_radio.pack(side="left", padx=10)
    decrypt_radio = ctk.CTkRadioButton(action_frame, text="Decrypt", variable=action_var, value="Decrypt")
    decrypt_radio.pack(side="left", padx=10)

    # Output Section  
    output_frame = ctk.CTkFrame(app, corner_radius=15)
    output_frame.pack(pady=20, padx=20, fill="x")

    output_label = ctk.CTkLabel(output_frame, text="Results:", font=("Helvetica", 14))
    output_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    output_text = ctk.CTkTextbox(output_frame, height=70, font=("Helvetica", 12))
    output_text.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    copy_button = ctk.CTkButton(output_frame, text="Copy", command=lambda: copy_to_clipboard(output_text.get("1.0", "end-1c")))
    copy_button.grid(row=0, column=2, padx=10)

    output_frame.grid_columnconfigure(1, weight=1)

    # Perform Action Button
    action_button = ctk.CTkButton(app, text="Perform Action", font=("Helvetica", 14), command=lambda: perform_action(input_text, output_text, password_entry, action_var))
    action_button.pack(pady=20)

    app.mainloop()


if __name__ == "__main__":
    create_app()
