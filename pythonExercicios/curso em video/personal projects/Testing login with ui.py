import tkinter
import customtkinter


def login():
    pass


def close_app():
    global closeApp
    closeApp = True


closeApp = False

# System Setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Login Screen")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="LABEL")
title.pack(padx=10, pady=5)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=450, height=40, placeholder_text="insert a video link", textvariable=url_var)
link.pack()

# Buttons
# LOGIN
button_login = customtkinter.CTkButton(app, text="Login")
button_login.pack(padx=10, pady=10)

# REGISTER
button_register = customtkinter.CTkButton(app, text="Cadastrar")
button_register.pack(padx=10, pady=10)

# Run app
if not closeApp:
    app.mainloop()

