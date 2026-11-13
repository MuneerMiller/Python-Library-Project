from database.connection import get_connection
from models.errors import LibraryError


def borrow_book(book_id, member_id):
    with get_connection() as conn:
        book = conn.execute("SELECT title, available FROM Books WHERE id = ?", (book_id,)).fetchone()
        if book is None:
            raise LibraryError(f"There is no book with ID {book_id}.")
        if not book["available"]:
            raise LibraryError(f"'{book['title']}' is already borrowed.")
        member = conn.execute("SELECT id FROM Members WHERE id = ?", (member_id,)).fetchone()
        if member is None:
            raise LibraryError(f"There is no member with ID {member_id}.")

        conn.execute("INSERT INTO Borrowings (book_id, member_id) VALUES (?, ?)", (book_id, member_id))
        conn.execute("UPDATE Books SET available = 0 WHERE id = ?", (book_id,))
        return book["title"]


def return_book(book_id):
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE Borrowings SET return_date = DATE('now') WHERE book_id = ? AND return_date IS NULL",
            (book_id,),
        )
        if cursor.rowcount == 0:
            raise LibraryError(f"Book {book_id} isn't currently borrowed.")
        conn.execute("UPDATE Books SET available = 1 WHERE id = ?", (book_id,))
        return conn.execute("SELECT title FROM Books WHERE id = ?", (book_id,)).fetchone()["title"]


def list_borrowed_books():
    """Books that are out right now, with who has them and since when."""
    with get_connection() as conn:
        return conn.execute(
            "SELECT Books.id, Books.title, Members.name, Borrowings.borrow_date "
            "FROM Borrowings "
            "JOIN Books ON Books.id = Borrowings.book_id "
            "JOIN Members ON Members.id = Borrowings.member_id "
            "WHERE Borrowings.return_date IS NULL "
            "ORDER BY Borrowings.borrow_date"
        ).fetchall()
