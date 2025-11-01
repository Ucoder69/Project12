import library as li
import csv 
import os
import ast

name=li.namecheck(li.striing("Name"))
if name:
    nam=name[0]
else: 
    nam=''
bk=''

# sql connector here!
id=li.Id()
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv"), "r", newline='')as file:
        reads= csv.reader(file,skipinitialspace=True)
        flag=0
        try:
            for read in reads:
                fname = ast.literal_eval(read[0])
                if fname[0]==nam and read[4]==str(id):
                    print("login succesfull")
                    print(f"welcome, {fname[0]}!")
                    bk=str(read[5])
                    flag=1
                    break
        except EOFError:
            print("This user credentials doesnt exists! (try relogging in or registering)")
        if flag!=1:
            print("This user credentials doesnt exists! (try relogging in or registering)")