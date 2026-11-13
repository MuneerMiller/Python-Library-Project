import sqlite3
from contextlib import contextmanager

from utils import config


@contextmanager
def get_connection():
    """Open the library database, commit on success, roll back on error and always close."""
    conn = sqlite3.connect(config.DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
