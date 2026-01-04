
import tkinter as tk
import register as rg

# function that receives data and returns an id
def hello(data):
    # dummy logic for id generation
    return hash(tuple(data)) % 100000



def submit():
    name = entry_name.get()
    class_ = entry_class.get()
    sec = entry_sec.get()
    roll = entry_roll.get()

    # data = [name, class_, sec, roll] 
    id_no = rg.register(name, class_, sec, roll) #the fn takes 4 arg we gave data as one arg :(

    result_label.config(text=f"Generated ID: {id_no} \n And only use your first name for login")


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