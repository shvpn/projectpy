import customtkinter as ctk
from PIL import Image
import math


# Function to interpolate between two colors
def interpolate_color(color1, color2, t):
    """Linearly interpolate between two HEX colors."""
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)

    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return f"#{r:02x}{g:02x}{b:02x}"  # Convert back to HEX


# Easing function (ease in-out cubic)
def ease_in_out_cubic(t):
    """Cubic easing function for smooth acceleration and deceleration."""
    if t < 0.5:
        return 4 * t * t * t
    return 1 - math.pow(-2 * t + 2, 3) / 2


# Smooth background transition
def smooth_background_transition(app, start_color, end_color, duration=2):
    """Smoothly change background color of the main window."""
    steps = 300  # Number of steps for transition
    delay = int(duration * 1000 / steps)  # Time delay between steps in milliseconds

    def update_color(step):
        if step <= steps:
            t = step / steps
            eased_t = ease_in_out_cubic(t)  # Apply easing for smoothness
            new_color = interpolate_color(start_color, end_color, eased_t)
            app.configure(bg=new_color)  # Change only the window background
            app.after(delay, update_color, step + 1)  # Schedule the next step

    update_color(0)  # Start the transition


# Main application
def create_app():
    def switch_event():
        if switch_var.get() == "on":
            ctk.set_appearance_mode("Light")
            smooth_background_transition(app, "#2b2b2b", "#ffffff", duration=2)  # Dark to Light
        else:
            ctk.set_appearance_mode("Dark")
            smooth_background_transition(app, "#ffffff", "#2b2b2b", duration=2)  # Light to Dark

    ctk.set_default_color_theme("green")  # Themes: "blue", "green", "dark-blue"

    app = ctk.CTk()
    app.title("SAR SOM NGAT")
    app.geometry("900x600")

    # Set default background color
    app.configure(bg="#2b2b2b")  # Default dark background

    # Header
    header_frame = ctk.CTkFrame(app, corner_radius=15)
    header_frame.pack(pady=20, padx=20, fill="x")

    # Load the logo image
    logo_image = ctk.CTkImage(Image.open("projectpy/image/logo.png"), size=(100, 100))  # Adjust size as needed

    # Add the logo image to a label
    logo_label = ctk.CTkLabel(header_frame, image=logo_image, text="", width=100, height=100)
    logo_label.pack(padx=10)

    # Add the title text next to the logo
    title_label = ctk.CTkLabel(header_frame, text="SAR SOM NGAT", font=("Helvetica", 40, "bold"))
    title_label.pack(padx=10)

    # Dark/Light Mode Switch
    switch_var = ctk.StringVar(value="off")
    switch = ctk.CTkSwitch(
        header_frame,
        text="Dark/Light",
        font=("Helvetica", 16),
        command=switch_event,
        variable=switch_var,
        offvalue="off",
        onvalue="on",
    )
    switch.pack(pady=20, padx=20, side="right")

    app.mainloop()


if __name__ == "__main__":
    create_app()
