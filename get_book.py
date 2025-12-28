# import library as li 
import login as lg
import mysql.connector

def check_bc(id, name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="library"  
    )

    cursor = mydb.cursor()
    cursor.execute(f"SELECT bc, book FROM books WHERE name = '{name}' AND id = {id}")
    data = cursor.fetchone()
    if data:
        bc, book= data
    else:
        bc=book=None
        
    cursor.close()
    mydb.close()
    return bc, book

def add_book(name, book, id):
    mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="library"  
    )

    cursor = mydb.cursor()
    cursor.execute(
        f"UPDATE books SET bc = 1, book = '{book}' WHERE name = '{name}' AND id = {id}")
    mydb.commit()
    cursor.close()
    mydb.close()
    

def remove_book(name,id):
    mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="library"  
    )

    cursor = mydb.cursor()
    cursor.execute(
        f"UPDATE books SET bc = 0, book = '' WHERE name = '{name}' AND id={id}")
    mydb.commit()
    cursor.close()
    mydb.close()
    
   
# if check_bc(name,id)==0:
#     add_book(name,book,id)
# else:
#     remove_book(name, id)
    

# force users to use check bc after every use of add_book and remove_book for latest data on their activities
