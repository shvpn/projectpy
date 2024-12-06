import customtkinter as ctk
from tkinter import messagebox, filedialog


class CustomDialog:
    ctk.set_appearance_mode("Dark")  # Modes: "Dark", "Light"
    ctk.set_default_color_theme("green")

    def __init__(self, title="Dialog", message="Enter your input:", btn_command=None):
        self.title = title
        self.message = message
        self.input_value = ""
        self.btn_command = btn_command  # Custom function for the button

    def show_dialog(self, parent=None):
        """Display the dialog window."""
        try:
            # Create a new top-level window as a child of the parent (if provided)
            self.dialog = ctk.CTkToplevel(parent) if parent else ctk.CTk()
            self.dialog.title(self.title)
            self.dialog.geometry("400x250")
            self.dialog.resizable(False, False)
            self.dialog.transient(parent)  # Set the dialog as a transient window (always on top of parent)
            self.dialog.grab_set()  # Prevent interaction with other windows until this is closed

            # Dialog content
            label = ctk.CTkLabel(self.dialog, text=self.message, font=("Arial", 14))
            label.pack(pady=10)

            # Input field
            self.input_field = ctk.CTkEntry(self.dialog, width=300, font=("Arial", 12))
            self.input_field.pack(pady=10)

            # Buttons
            select_button = ctk.CTkButton(
                self.dialog,
                text="Choose Directory",
                command=self.run_custom_function,
            )
            select_button.pack(pady=5)

            submit_button = ctk.CTkButton(
                self.dialog, text="Submit", command=lambda: self.submit()
            )
            submit_button.pack(pady=5)

            cancel_button = ctk.CTkButton(
                self.dialog, text="Cancel", command=self.dialog.destroy
            )
            cancel_button.pack(pady=5)

            self.dialog.mainloop()
        except Exception as e:
            messagebox.showerror("Dialog Error", str(e))
        return self.input_value

    def run_custom_function(self):
        """Run the custom command (e.g., directory selection)."""
        if callable(self.btn_command):
            result = self.btn_command()  # Execute the passed function
            if result:
                self.input_field.delete(0, ctk.END)
                self.input_field.insert(0, result)

    def submit(self):
        """Capture input value and close the dialog."""
        self.input_value = self.input_field.get()
        self.dialog.destroy()


# Example of a custom function to choose a directory
def choose_directory():
    pass


# Example of using the dialog
if __name__ == "__main__":
    app = ctk.CTk()  # Main application window
    app.geometry("500x400")
    app.title("Main App")

    def open_dialog():
        dialog = CustomDialog(title="Custom Dialog", message="Enter your name:", btn_command=choose_directory)
        user_input = dialog.show_dialog(parent=app)
        print(f"User Input: {user_input}")

    open_button = ctk.CTkButton(app, text="Open Dialog", command=open_dialog)
    open_button.pack(pady=20)

    app.mainloop()
