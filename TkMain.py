from tkinter import *
from tkinter import ttk

window = Tk()
# theme
window.tk.call("source", "XII Project\\Azure\\Zure.tcl")
window.tk.call("set_theme", "dark")

# Window
window.geometry("900x900")
window.title("Library Management")

# Icon
icon = 'MDT\\Assets\\library.ico'
Labelimg = PhotoImage(file='MDT\\Assets\\library__1_-removebg-preview.png')
Admimg = PhotoImage(file="MDT\\Assets\\Admin.png")
Stdimg = PhotoImage(file="MDT\\Assets\\Student.png")

window.config(background="#51504f")
window.wm_iconbitmap(icon)

# Header
label = Label(
    text=" Library Management System",
    font=("Arial", 40, "bold", "underline"),
    fg="White",
    bg="#51504f",
    image=Labelimg,
    compound="left"
)
label.pack(pady=40)

# Frame for buttons (auto centers)
button_frame = Frame(window, bg="#51504f")
button_frame.pack(expand=True)  # centers vertically & horizontally

#Styles
style = ttk.Style()
style.configure("TButton", font=("Arial", 20, "bold"))

#Buttons
def Exi():
    window.destroy()
# Admin Button
button1 = ttk.Button(
    button_frame,
    text="Admin",
    image=Admimg,
    compound=LEFT,
    style="TButton"
)
button1.pack(pady=20)

# Student Button
button2 = ttk.Button(
    button_frame,
    text="Student",
    image=Stdimg,
    compound=LEFT,
    style="TButton"
)
button2.pack(pady=20)

button3 = ttk.Button(
    button_frame,
    text="Exit",
    style="TButton",
    command=Exi
)
button3.pack(pady=20)






window.mainloop()
