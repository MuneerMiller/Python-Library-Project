import os
from pathlib import Path

# The database lives next to the project files unless LIBRARY_DB points elsewhere.
DB_NAME = os.environ.get("LIBRARY_DB", str(Path(__file__).resolve().parent.parent / "library.db"))
