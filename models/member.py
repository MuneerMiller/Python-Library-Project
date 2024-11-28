import sqlite3  # Ensure sqlite3 is imported

def add_member(name, email):
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Members (name, email) VALUES (?, ?)", (name, email))
        conn.commit()

def list_members():
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Members")
        return cursor.fetchall()
