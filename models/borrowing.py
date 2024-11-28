def borrow_book(book_id, member_id):
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT available FROM Books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        if book and book[0]:
            cursor.execute(
                "INSERT INTO Borrowings (book_id, member_id) VALUES (?, ?)",
                (book_id, member_id)
            )
            cursor.execute("UPDATE Books SET available = 0 WHERE id = ?", (book_id,))
            conn.commit()
        else:
            raise Exception("Book is not available")

def return_book(book_id):
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Borrowings SET return_date = DATE('now') WHERE book_id = ? AND return_date IS NULL",
            (book_id,)
        )
        cursor.execute("UPDATE Books SET available = 1 WHERE id = ?", (book_id,))
        conn.commit()
