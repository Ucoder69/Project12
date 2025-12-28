import library as li
import mysql.connector
import random

def register():
    inp=li.get_input()
    idr=random.randint(1000,99999)
    inp.append(idr)
    print(inp, type(inp))

    mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="library"
)

    cursor = mydb.cursor()
    name, mname, surname = inp[0]
    class_ = inp[1]
    sec = inp[2]
    roll = inp[3]
    id_ = inp[4]

    cursor.execute(
    """
    INSERT INTO students (id, name, mname, surname, class, sec, roll)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """,
    (id_, name, mname, surname, class_, sec, roll)
)

    mydb.commit()

    cursor.execute(
    """
    INSERT INTO books (id, name, bc, book)
    VALUES (%s, %s, 0, '')
    """,
    (id_, name)
)

    mydb.commit()
    cursor.close()
    mydb.close()

register()