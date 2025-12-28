import mysql.connector

def create_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password"
    )

    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS library")
    cursor.execute("USE library")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registry (
    e_id INT AUTO_INCREMENT PRIMARY KEy
    id INT ,
    name VARCHAR(50),
    mname VARCHAR(50),
    surname VARCHAR(50),
    class INT,
    sec VARCHAR(10),
    roll INT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
    entry_id INT AUTO_INCREMENT,
    id INT,
    name VARCHAR(50),
    bc INT DEFAULT 0,
    FOREIGN KEY (id, name) REFERENCES students(id, name),
    book VARCHAR(255) DEFAULT '',
    PRIMARY KEY (entry_id)
    )
    """)

    mydb.commit()
    cursor.close()
    mydb.close()

create_db()

# run this just after the app starts no matter who
