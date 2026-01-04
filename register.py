import mysql.connector
import random

def namecheck(str_value: str):
    if p:=str_value.strip().split(" "):
        Name=p[0]
        Surname=p[-1]
        middle="".join(p[1:-1]) if len(str_value)>2 else ""
        # print(Name.title())
        return [Name, middle, Surname]
    else:
        print("you have entered something wrong")
        
def register(sname :str , class_, sec, roll):
    id_=random.randint(1000,99999)
    try:
        name, mname , surname = namecheck(sname) # type: ignore
    except:
        name, mname , surname =''
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="your_username",
#     password="your_password",
#     database="library"
# )

#     cursor = mydb.cursor()
#     cursor.execute(
#     """
#     INSERT INTO students (id, name, mname, surname, class, sec, roll)
#     VALUES (%s, %s, %s, %s, %s, %s, %s)
#     """,
#     (id_, name, mname, surname, class_, sec, roll)
# )

#     mydb.commit()

#     cursor.execute(
#     """
#     INSERT INTO books (id, name, bc, book)
#     VALUES (%s, %s, 0, '')
#     """,
#     (id_, name)
# )

#     mydb.commit()
#     cursor.close()
#     mydb.close()
    return name, id_