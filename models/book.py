from database.connection import get_connection
from models.errors import LibraryError


def add_book(title, author):
    """Add a book and return its new ID."""
    title, author = title.strip(), author.strip()
    if not title or not author:
        raise LibraryError("A book needs both a title and an author.")
    with get_connection() as conn:
        cursor = conn.execute("INSERT INTO Books (title, author) VALUES (?, ?)", (title, author))
        return cursor.lastrowid


def list_books():
    with get_connection() as conn:
        return conn.execute("SELECT id, title, author, available FROM Books ORDER BY title").fetchall()


def search_books(term):
    """Find books whose title or author contains the search term, ignoring case."""
    pattern = f"%{term.strip()}%"
    with get_connection() as conn:
        return conn.execute(
            "SELECT id, title, author, available FROM Books "
            "WHERE title LIKE ? OR author LIKE ? ORDER BY title",
            (pattern, pattern),
        ).fetchall()
