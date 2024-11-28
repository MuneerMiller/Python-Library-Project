
# Library Management System

A command-line interface (CLI) application to manage a library system using **Python** and **SQLite**. The system allows users to perform tasks like adding books, registering members, borrowing/returning books, and listing books and members in a structured, user-friendly table format.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Setup Instructions](#setup-instructions)
3. [Usage](#usage)
   - [Example Workflows](#example-workflows)
4. [Project Structure](#project-structure)
5. [Known Issues & Limitations](#known-issues--limitations)
6. [Future Enhancements](#future-enhancements)

---

## Features

1. **Add a Book**:
   - Add a book to the library database with its title and author.
2. **Register a Member**:
   - Register library members by entering their name and email.
3. **Borrow a Book**:
   - Borrow a book by providing the book ID and member ID, ensuring only available books can be borrowed.
4. **Return a Book**:
   - Return a borrowed book to make it available again.
5. **List All Books**:
   - Display all books in a clean, table format with their title and author.
6. **List Registered Members**:
   - Display all registered members in a table format with their name and email.
7. **Exit**:
   - Exit the application gracefully.

---

## Installation

### Prerequisites

- Python 3.6 or higher
- SQLite (Python’s built-in library is sufficient)
- `tabulate` Python library (for clean table display)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd LibraryManagementSystem
2. **Install dependencies**:
   ```bash
   pip install tabulate
3. **Initialize the database**: Run the script to create the required tables
   ```bash
   python init_db.py
4. **Run the application**:
   ```bash
   python main.py
## Usage

1. **Launch the program**:
   ```bash
   python main.py
2. **Use the menu to navigate between options**:
   - Enter the number corresponding to the desired action.

### Example Workdlows

**Add a book**
- Select option 1.
- Enter the book title and author.
- The book will be added to the library.

**Borrow a Book**
- Select option 3.
- Enter a valid book ID and member ID.
- The book will be marked as borrowed.

**List All Books**
- Select option 5.
- See a table of all books, including their titles and authors.
- List Registered Members
- Select option 6.
- View a table of all registered members with their names and emails.

## Project Structure

```bash
LibraryManagementSystem/
│
├── main.py                  # Entry point of the application
├── init_db.py               # Script to initialize the SQLite database
├── database/
│   ├── connection.py        # Handles SQLite database connections
│   ├── setup.sql            # (Optional) SQL script for database schema
│
├── models/
│   ├── book.py              # Book-related operations (add, list books)
│   ├── member.py            # Member-related operations (add, list members)
│   ├── borrowing.py         # Borrowing-related operations (borrow, return books)
│
├── utils/
│   ├── helpers.py           # Helper functions (e.g., input sanitization)
│   ├── config.py            # Configuration (e.g., database name)
│
└── README.md                # Documentation
```

## Known Issues & Limitations

- Non-numeric Input: Borrowing/returning books requires numeric IDs; invalid inputs result in errors.
- Member Deletion: Deleting members or books is not supported yet.
- Overdue Books: Currently, there’s no functionality to track overdue books or calculate fines.

## Future Enhancements

- Add functionality to handle overdue books and calculate fines.
- Implement a search feature for books and members.
- Enhance borrowing/returning to allow specifying due dates.
- Support multiple copies of the same book.
- Add admin authentication for restricted actions.
