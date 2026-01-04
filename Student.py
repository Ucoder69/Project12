from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import re
import register as rg

# ----------------- VALIDATION -----------------

def namecheck(str_value: str):
    p = str_value.strip().split()
    if not p:
        raise ValueError("Invalid name")
    name = p[0]
    surname = p[-1]
    middle = "".join(p[1:-1]) if len(p) > 2 else ""
    return [name, middle, surname]

def valid_section(sec):
    if re.fullmatch(r"[A-Za-z0-9]+", sec):
        return sec.upper()
    raise ValueError("Only alphanumeric allowed in Section")

# ----------------- STUDENT WINDOW -----------------

def Student():
    root = Toplevel()
    root.title("Student Portal")
    root.geometry("500x550")
    root.config(bg="#333333")

    Label(
        root,
        text="Student Login",
        font=("Arial", 26, "bold"),
        fg="white",
        bg="#333333"
    ).pack(pady=30)

    # ---------- LOGIN FIELDS ----------
    Label(root, text="Student ID", fg="white", bg="#333333",
          font=("Arial", 14)).pack()
    id_entry = Entry(root, font=("Arial", 14))
    id_entry.pack(pady=5)

    Label(root, text="Username", fg="white", bg="#333333",
          font=("Arial", 14)).pack()
    user_entry = Entry(root, font=("Arial", 14))
    user_entry.pack(pady=5)

    # ---------- LOGIN FUNCTION ----------
    def login_student():
        sid = id_entry.get().strip()
        uname = user_entry.get().strip().title()

        if not sid or not uname:
            messagebox.showerror("Error", "All fields required")
            return

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="your_username",
                password="your_password",
                database="library"
            )
            cursor = mydb.cursor()

            cursor.execute(
                "SELECT book FROM books WHERE id=%s AND name=%s",
                (sid, uname)
            )
            result = cursor.fetchone()

            cursor.close()
            mydb.close()

            if not result:
                messagebox.showerror("Error", "Invalid credentials")
                return

            root.destroy()
            student_dashboard(sid, result[0])

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # ---------- REGISTER WINDOW ----------
    def register_student():
        reg = Toplevel()
        reg.title("Register Student")
        reg.geometry("450x550")
        reg.config(bg="#444444")

        Label(
            reg,
            text="Register",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#444444"
        ).pack(pady=20)

        entries = {}
        fields = ["Full Name", "Class", "Section", "Roll"]

        for f in fields:
            Label(reg, text=f, fg="white", bg="#444444",
                  font=("Arial", 12)).pack()
            e = Entry(reg, font=("Arial", 14))
            e.pack(pady=5)
            entries[f] = e

        def submit_register():
            try:
                full = namecheck(entries["Full Name"].get())
                class_ = int(entries["Class"].get())
                sec = valid_section(entries["Section"].get())
                roll = int(entries["Roll"].get())

                sid = rg.register_student(full, class_, sec, roll)

                messagebox.showinfo(
                    "Registration Successful",
                    f"Student Registered!\nYour Student ID: {sid}"
                )
                reg.destroy()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(reg, text="Submit",
                   command=submit_register).pack(pady=20)

    # ---------- MAIN BUTTONS ----------
    ttk.Button(root, text="Login",
               command=login_student).pack(pady=15)
    ttk.Button(root, text="Register",
               command=register_student).pack()

# ----------------- DASHBOARD -----------------

def student_dashboard(sid, book_name):
    dash = Toplevel()
    dash.title("Student Dashboard")
    dash.geometry("500x400")
    dash.config(bg="#51504f")

    Label(
        dash,
        text=f"Student ID: {sid}",
        font=("Arial", 16),
        bg="#51504f",
        fg="white"
    ).pack(pady=20)

    has_book = bool(book_name)

    def check_status():
        messagebox.showinfo(
            "Status",
            "Book Issued" if has_book else "No Book Issued"
        )

    def add_book():
        messagebox.showinfo("Added", "Book Added")
        btn_add.config(state=DISABLED)
        btn_status.config(state=NORMAL)

    def remove_book():
        messagebox.showinfo("Removed", "Book Removed")
        btn_add.config(state=NORMAL)
        btn_status.config(state=DISABLED)

    btn_status = ttk.Button(
        dash, text="Check Status", command=check_status)
    btn_add = ttk.Button(
        dash, text="Add Book", command=add_book)
    btn_remove = ttk.Button(
        dash, text="Remove Book", command=remove_book)

    btn_status.pack(pady=10)
    btn_add.pack(pady=10)
    btn_remove.pack(pady=10)

    # ---- BUTTON STATE LOGIC ----
    if has_book:
        btn_add.config(state=DISABLED)
    else:
        btn_status.config(state=DISABLED)
