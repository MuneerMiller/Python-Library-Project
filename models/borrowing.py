import sqlite3


def borrow_book(book_id, member_id):
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        # Check if the book is available
        cursor.execute("SELECT available FROM Books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        if not book:
            raise Exception("Book ID not found.")
        if book[0] == 0:
            raise Exception("Book is not available for borrowing.")
        # Record the borrowing
        cursor.execute(
            "INSERT INTO Borrowings (book_id, member_id) VALUES (?, ?)",
            (book_id, member_id)
        )
        # Mark the book as unavailable
        cursor.execute("UPDATE Books SET available = 0 WHERE id = ?", (book_id,))
        conn.commit()


def return_book(book_id):
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Borrowings SET return_date = DATE('now') WHERE book_id = ? AND return_date IS NULL",
            (book_id,)
        )
        cursor.execute("UPDATE Books SET available = 1 WHERE id = ?", (book_id,))
        conn.commit()
