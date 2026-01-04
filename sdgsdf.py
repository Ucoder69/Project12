import tkinter as tk
import register as rg
def submit():
    name = entry_name.get()
    class_ = entry_class.get()
    sec = entry_sec.get()
    roll = entry_roll.get()

    data = [name, class_, sec, roll]
    id_no = rg.register(data)

    result_label.config(text=f"Generated ID: {id_no}")


# --- UI ---
root = tk.Tk()
root.title("Student Form")
root.geometry("300x300")

tk.Label(root, text="Full Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Class").pack()
entry_class = tk.Entry(root)
entry_class.pack()

tk.Label(root, text="Section").pack()
entry_sec = tk.Entry(root)
entry_sec.pack()

tk.Label(root, text="Roll").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Button(root, text="Submit", command=submit).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()