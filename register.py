import library as li
import mysql.connector
import random

def register(name, class_, sec, roll):
    id_=random.randint(1000,99999)
    name, name , surname =name
    mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="library"
)

    cursor = mydb.cursor()
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
    return id_

register(name, class_, sec, roll)


