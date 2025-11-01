import library as li
import random
import csv 
import os

inp=li.get_input()
if any(x is not None for x in inp):
    idr=random.randint(1000,9999)
    inp.append(idr)
    print(f"Your login info::\nName: {inp[0][0]}\nId: {idr}")
    # to sql database connect here!
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv"), "a", newline='')as file:
        writer=csv.writer(file)
        writer.writerow(inp)
else:
    print("something is wrong")