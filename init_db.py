import sqlite3

def initialize_database():
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.executescript("""
        CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            available INTEGER DEFAULT 1
        );

        CREATE TABLE IF NOT EXISTS Members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS Borrowings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            member_id INTEGER NOT NULL,
            borrow_date DATE DEFAULT (DATE('now')),
            return_date DATE,
            FOREIGN KEY (book_id) REFERENCES Books (id),
            FOREIGN KEY (member_id) REFERENCES Members (id)
        );
        """)
        print("Database initialized successfully!")

if __name__ == "__main__":
    initialize_database()
