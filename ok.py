# import customtkinter as ctk

# # Main Application
# def create_app():
#     app = ctk.CTk()
#     app.title("CustomTkinter Example")
#     app.geometry("600x600")

#     # Tabs using CTkTabview
#     tabview = ctk.CTkTabview(app, width=400, height=300)
#     tabview.pack(pady=20, padx=20, fill="x")

#     tab1 = tabview.add("Tab 1")
#     tab2 = tabview.add("Tab 2")
#     tab3 = tabview.add("Tab 3")
#     tabview.set("Tab 1")  # Set default tab

#     # Widgets for Tab 1
#     optionmenu_var = ctk.StringVar(value="Option 1")
#     optionmenu = ctk.CTkOptionMenu(tab1, values=["Option 1", "Option 2", "Option 3"], variable=optionmenu_var)
#     optionmenu.pack(pady=10, padx=20)

#     combobox_var = ctk.StringVar(value="Select Item")
#     combobox = ctk.CTkComboBox(tab1, values=["Item 1", "Item 2", "Item 3"], variable=combobox_var)
#     combobox.pack(pady=10, padx=20)

#     # Widgets for Tab 2
#     radio_var = ctk.StringVar(value="Radio 1")
#     radio_frame = ctk.CTkFrame(tab2, corner_radius=10)
#     radio_frame.pack(pady=20, padx=20, fill="both", expand=True)

#     radio_label = ctk.CTkLabel(radio_frame, text="CTkRadioButton Group:")
#     radio_label.pack(pady=5)

#     radio1 = ctk.CTkRadioButton(radio_frame, text="CTkRadioButton", variable=radio_var, value="Radio 1")
#     radio1.pack(pady=5)

#     radio2 = ctk.CTkRadioButton(radio_frame, text="CTkRadioButton", variable=radio_var, value="Radio 2")
#     radio2.pack(pady=5)

#     radio3 = ctk.CTkRadioButton(radio_frame, text="CTkRadioButton", variable=radio_var, value="Radio 3")
#     radio3.pack(pady=5)

#     # Widgets for Tab 3
#     checkbox_frame = ctk.CTkFrame(tab3, corner_radius=10)
#     checkbox_frame.pack(pady=20, padx=20, fill="both", expand=True)

#     checkbox_label = ctk.CTkLabel(checkbox_frame, text="CTkCheckBox Group:")
#     checkbox_label.pack(pady=5)

#     checkbox1 = ctk.CTkCheckBox(checkbox_frame, text="CTkCheckBox")
#     checkbox1.pack(pady=5)

#     checkbox2 = ctk.CTkCheckBox(checkbox_frame, text="CTkCheckBox")
#     checkbox2.pack(pady=5)

#     checkbox3 = ctk.CTkCheckBox(checkbox_frame, text="CTkCheckBox", state="disabled")
#     checkbox3.pack(pady=5)

#     # Scrollable Frame
#     scrollable_frame = ctk.CTkScrollableFrame(app, label_text="CTkScrollableFrame")
#     scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

#     for i in range(5):  # Adding multiple switches to the scrollable frame
#         switch = ctk.CTkSwitch(scrollable_frame, text=f"CTkSwitch {i}")
#         switch.grid(row=i, column=0, padx=10, pady=10)

#     app.mainloop()


# if __name__ == "__main__":
#     create_app()

import customtkinter as ctk

# Initialize the app
app = ctk.CTk()
app.geometry("400x300")

def show_frame1():
    frame2.pack_forget()
    frame1.pack()

def show_frame2():
    frame1.pack_forget()
    frame2.pack()

# Frame 1
frame1 = ctk.CTkFrame(app, width=300, height=200)
frame1.pack()
label1 = ctk.CTkLabel(frame1, text="This is Frame 1")
label1.pack()

# Frame 2
frame2 = ctk.CTkFrame(app, width=300, height=200)
label2 = ctk.CTkLabel(frame2, text="This is Frame 2")
label2.pack()

# Buttons to switch between frames
btn1 = ctk.CTkButton(app, text="Show Frame 1", command=show_frame1)
btn1.pack(side="left", padx=10)

btn2 = ctk.CTkButton(app, text="Show Frame 2", command=show_frame2)
btn2.pack(side="right", padx=10)

app.mainloop()
