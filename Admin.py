from tkinter import *
from tkinter import ttk, messagebox

# --- Admin credentials ---
ADMIN_ID = "admin123"
ADMIN_PASS = "password123"

def Admin():
    root = Toplevel()
    root.title("Admin Login")
    root.geometry("500x500")
    root.wm_iconbitmap("MDT\\Assets\\Admin.ico")
    root.config(bg="#333333")

    Admimg = PhotoImage(file="MDT\\Assets\\Admin.png")
    root.Admimg = Admimg  

    Label(
        root,
        text=" Admin Panel Login",
        font=("Arial", 28, "bold"),
        fg="white",
        bg="#333333",
        image=Admimg,
        compound="left"
    ).pack(pady=30)



    Label(root, text="Admin ID:", bg="#333333", fg="white", font=("Arial", 16)).pack(pady=5)

    id_entry = Entry(root, font = ("Arial", 16), show="*")

    id_entry.pack(pady=0)





    Label(root, text="Password:", bg="#333333", fg="white", font=("Arial", 16)).pack(pady=5)

    pass_entry = Entry(root, font=("Arial", 16), show="*")

    pass_entry.pack(pady=0)






    def check_login():
        entered_id = id_entry.get().strip()
        entered_pass = pass_entry.get().strip()

        if entered_id == ADMIN_ID and entered_pass == ADMIN_PASS:
            messagebox.showinfo("Access Granted", "Welcome, Admin!")
            root.destroy() 
            open_admin_panel()
        else:
            messagebox.showerror("Access Denied", "Invalid ID or Password")

    # --- Login button ---
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 16, "bold"))
    ttk.Button(root, text="Login", style="TButton", command=check_login).pack(pady=20)


def open_admin_panel():
    panel = Toplevel()
    panel.title("Admin Panel")
    panel.geometry("900x900")
    panel.wm_iconbitmap("MDT\\Assets\\Admin.ico")
    panel.config(bg="#51504f")

    Label(
        panel,
        text="Welcome to Admin Panel",
        font=("Arial", 30, "bold"),
        fg="white",
        bg="#51504f"
    ).pack(pady=50)

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 18, "bold"))

    ttk.Button(panel, text="Manage Books", style="TButton").pack(pady=10)
    ttk.Button(panel, text="View Students", style="TButton").pack(pady=10)
    ttk.Button(panel, text="Logout", style="TButton", command=panel.destroy).pack(pady=20)
