from tkinter import *
from tkinter import filedialog, messagebox, ttk
import tkinter as tk
from rembg import remove
from PIL import Image, ImageTk
import os


# Function to browse for an image
def browse_image():
    input_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*"))
    )
    if input_path:
        entry_input_path.delete(0, tk.END)
        entry_input_path.insert(0, input_path)
        show_image(input_path, input_image_label)

# Function to display the selected image
def show_image(image_path, label):
    try:
        img = Image.open(image_path)
        img.thumbnail((400, 350))
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img
    except Exception as e:
        messagebox.showerror("Error", f"Could not open image: {e}")

# Function to process and remove background
def remove_bg():
    input_path = entry_input_path.get()
    output_path = entry_output_path.get()

    if not input_path or not output_path:
        messagebox.showwarning("Input Error", "Please specify both input and output paths")
        return

    try:
        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)
        messagebox.showinfo("Success", f"Background removed and saved at {output_path}")
        show_image(output_path, output_image_label)
    except Exception as e:
        messagebox.showerror("Processing Error", f"Error removing background: {e}")


# Function to browse for output directory
def browse_output_path():
    output_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*"))
    )
    if output_path:
        entry_output_path.delete(0, tk.END)
        entry_output_path.insert(0, output_path)


# Creating main window
root = tk.Tk()
root.title("Image Background Remover")
root.geometry("930x650")

# Main frame for the image remover UI
myframe = Frame(root, relief=RIDGE)
myframe.pack(padx=10, pady=10)

# Logo image
myphoto = PhotoImage(file="projectpy/image/logo.png")
myphoto = myphoto.subsample(11, 11)
Label(myframe, image=myphoto, width=120, height=120).grid(row=0, column=0)
Label(myframe, text="លុបផ្ទៃខាងក្រោមរបស់រូបភាព", font=("Romnea", 25), fg="blue").grid(row=0, column=1, padx=10)
Label(myframe, text="ផលិតដោយ៖ លោកគ្រូ លាង បញ្ញរ៉ា    ជំនាន់ទី១.០", font=("Romnea", 14), fg="darkblue").grid(row=1, column=1, padx=10)
# Input image path label frame
labelframe1 = tk.LabelFrame(master=root, text="ជ្រើសរើសរូបភាព", font=("Romnea", 12))
labelframe1.pack(fill="x", padx=10, pady=10)

# Input image path entry and browse button
tk.Label(labelframe1, text="ទីតាំងរូបភាព៖", font=("Romnea", 11)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_input_path = tk.Entry(labelframe1, font=("Arial", 12), width=70)
entry_input_path.grid(row=0, column=1, padx=10, pady=10)
browse_input_btn = tk.Button(labelframe1, text="ស្វែងរករូបភាព", command=browse_image, font=("Romnea", 10))
browse_input_btn.grid(row=0, column=2, padx=10, pady=10)

# Output image path entry and browse button
tk.Label(labelframe1, text="ទីតាំងរូបភាពថ្មី៖", font=("Romnea", 11)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_output_path = tk.Entry(labelframe1, font=("Arial", 12), width=70)
entry_output_path.grid(row=1, column=1, padx=10, pady=10)
browse_output_btn = tk.Button(labelframe1, text="រក្សាទុកឈ្មោះថ្មី", command=browse_output_path, font=("Romnea", 10))
browse_output_btn.grid(row=1, column=2, padx=10, pady=10)

# Label frame for input image preview
input_image_frame = tk.LabelFrame(root, text="      បង្ហាញរូបភាពមុនពេលលុបផ្ទៃខាងក្រោយ       ", font=("Romnea", 14))
input_image_frame.pack(side=LEFT, padx=10, pady=10, fill="both", expand=False )

input_image_label = tk.Label(input_image_frame)
input_image_label.pack(side=LEFT, padx=10, pady=10)


# Label frame for output image preview
output_image_frame = tk.LabelFrame(root, text="                             រូបភាពថ្មី                             ", font=("Romnea", 14))
output_image_frame.pack(side=LEFT, padx=10, pady=10, fill="both", expand=True)

output_image_label = tk.Label(output_image_frame)
output_image_label.pack(padx=10, pady=10)

# Button to process and remove background
remove_bg_btn = tk.Button(root, text="លុបផ្ទៃខាងក្រោយ",font=("Romnea",12), command=remove_bg, bg="green", fg="white")
remove_bg_btn.pack(side=LEFT)

# Running the Tkinter loop
root.mainloop()
