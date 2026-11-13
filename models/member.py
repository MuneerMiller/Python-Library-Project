import sqlite3

from database.connection import get_connection
from models.errors import LibraryError
from utils.helpers import is_valid_email


def add_member(name, email):
    """Register a member and return their new ID."""
    name, email = name.strip(), email.strip().lower()
    if not name:
        raise LibraryError("A member needs a name.")
    if not is_valid_email(email):
        raise LibraryError(f"'{email}' doesn't look like an email address.")
    try:
        with get_connection() as conn:
            cursor = conn.execute("INSERT INTO Members (name, email) VALUES (?, ?)", (name, email))
            return cursor.lastrowid
    except sqlite3.IntegrityError:
        raise LibraryError(f"A member with the email '{email}' is already registered.") from None


def list_members():
    with get_connection() as conn:
        return conn.execute("SELECT id, name, email FROM Members ORDER BY name").fetchall()
