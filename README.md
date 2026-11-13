# Library Management System

A command-line app for running a small library, written in **Python** with an **SQLite** database. Librarians can add books, register members, lend and return books, see what's out and search the catalogue, all from a simple numbered menu with tidy tables.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
[![Tests](https://github.com/MuneerMiller/Python-Library-Project/actions/workflows/tests.yml/badge.svg)](https://github.com/MuneerMiller/Python-Library-Project/actions/workflows/tests.yml)

```
+------+--------------------------+---------------+-----------+
|   ID | Title                    | Author        | Status    |
+======+==========================+===============+===========+
|    2 | Cry, the Beloved Country | Alan Paton    | Available |
+------+--------------------------+---------------+-----------+
|    1 | Things Fall Apart        | Chinua Achebe | Borrowed  |
+------+--------------------------+---------------+-----------+
```

## Features

| Option | What it does |
| --- | --- |
| **1. Add a book** | Adds a title and author, and shows the new book's ID |
| **2. Register a member** | Saves a name and email. Emails are checked and must be unique |
| **3. Borrow a book** | Lends a book to a member by their IDs, if the book is available |
| **4. Return a book** | Marks a borrowed book as returned |
| **5. List all books** | Shows every book with its ID and whether it's available or borrowed |
| **6. List registered members** | Shows every member with their ID and email |
| **7. List borrowed books** | Shows what's out, who has it and since when |
| **8. Search books** | Finds books by any part of the title or author |
| **0. Exit** | Closes the app (Ctrl+C works too) |

Mistakes get a clear message instead of a crash: an unknown ID, a book that's already out, returning a book that isn't borrowed, a duplicate or invalid email, or a blank title.

## Getting started

You need Python 3.10 or newer.

```bash
git clone https://github.com/MuneerMiller/Python-Library-Project.git
```

```bash
cd Python-Library-Project
```

```bash
pip install -r requirements.txt
```

```bash
python main.py
```

The app creates `library.db` the first time it runs. You can also create it on its own with `python init_db.py`. To keep the database somewhere else, set `LIBRARY_DB` to a file path before running.

## Running the tests

```bash
python -m unittest -v
```

The tests give each case its own temporary database. They cover adding and searching books, member validation, and the borrowing rules. GitHub Actions runs them on Python 3.10 and 3.13 for every push and pull request.

## How it's built

```
Python-Library-Project/
├── main.py              # Menu and user input
├── init_db.py           # Creates the tables from database/setup.sql
├── database/
│   ├── connection.py    # Opens SQLite, commits or rolls back, and closes
│   └── setup.sql        # Schema: Books, Members and Borrowings
├── models/
│   ├── book.py          # Add, list and search books
│   ├── member.py        # Register and list members
│   ├── borrowing.py     # Borrow, return and list borrowed books
│   └── errors.py        # LibraryError for problems the user can fix
├── utils/
│   ├── config.py        # Database location
│   └── helpers.py       # Input and email helpers
└── tests/
    └── test_library.py  # unittest suite
```

Some design choices:

- **Parameterised SQL everywhere**, so input such as `'; DROP TABLE Books; --` is stored as text, never run.
- **One connection helper** commits when everything works and rolls back when something fails, so a half-finished loan can't leave a book marked as out.
- **Foreign keys are switched on**, so a loan can't point at a book or member that doesn't exist.
- **The menu and the data layer are separate.** `models/` never prints or asks for input, which is what makes it easy to test.

## Ideas for next steps

- Due dates, overdue lists and fines
- Several copies of the same book
- Editing and removing books and members
- A web front end on top of the same `models/` code

## Licence

Copyright © 2026 Mogamat Muneer Miller. All rights reserved. The code is public so you can read it and learn from it, but it is not open source. See [LICENSE](LICENSE).

## Contact

Built by **[Muneer Miller](https://github.com/MuneerMiller)** · [muneermiller.github.io](https://muneermiller.github.io/)
