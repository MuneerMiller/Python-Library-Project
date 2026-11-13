from pathlib import Path

from database.connection import get_connection

SCHEMA = Path(__file__).resolve().parent / "database" / "setup.sql"


def initialize_database():
    """Create the tables if they don't exist yet. Safe to run more than once."""
    with get_connection() as conn:
        conn.executescript(SCHEMA.read_text())


if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully!")
