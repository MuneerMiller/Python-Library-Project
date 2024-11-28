import sqlite3  # Import sqlite3 module to connect to the database

def add_book(title, author):
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Books (title, author) VALUES (?, ?)", (title, author))
        conn.commit()

def list_books():
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books")
        return cursor.fetchall()
