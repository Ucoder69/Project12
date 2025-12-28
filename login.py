import library as li
import mysql.connector

def login(nam, id):
    mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="library"  
    )
    cursor = mydb.cursor()
    cursor.execute(f"SELECT 1 FROM registry WHERE name = '{nam}' AND id={id} LIMIT 1")
    exists = cursor.fetchone() is not None
    
    if exists:
        print(f"welcome, {nam}!") #printing welcome - change this as you want subh
        cursor.execute(
        f"SELECT bc, book FROM books WHERE name = '{nam}' AND id = {id}" )
        data = cursor.fetchone()
        cursor.close()
        mydb.close()
        if data:
            bc, book= data
        else:
            bc=book=None       
        return bc, book
    else:
        cursor.close()
        mydb.close()
        print("credentials are not found")
        return None
    
# the data here we got is the book-count as bc, book(if), nam and id. use this for get_book and etc, there exists a separate check_bc for same purpose but you can remove if you want

# ~sup 28th dec
