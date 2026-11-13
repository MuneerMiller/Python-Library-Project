from tabulate import tabulate

from init_db import initialize_database
from models.book import add_book, list_books, search_books
from models.borrowing import borrow_book, list_borrowed_books, return_book
from models.errors import LibraryError
from models.member import add_member, list_members
from utils.helpers import prompt_input, prompt_int

MENU = """
Library Management System
1. Add a book
2. Register a member
3. Borrow a book
4. Return a book
5. List all books
6. List registered members
7. List borrowed books
8. Search books
0. Exit"""


def show_books(books, empty_message="No books found."):
    if not books:
        print(empty_message)
        return
    rows = [(b["id"], b["title"], b["author"], "Available" if b["available"] else "Borrowed") for b in books]
    print(tabulate(rows, headers=["ID", "Title", "Author", "Status"], tablefmt="grid"))


def handle_add_book():
    book_id = add_book(prompt_input("Book title: "), prompt_input("Author: "))
    print(f"Book added with ID {book_id}.")


def handle_add_member():
    member_id = add_member(prompt_input("Member name: "), prompt_input("Member email: "))
    print(f"Member registered with ID {member_id}.")


def handle_borrow():
    book_id = prompt_int("Book ID: ")
    member_id = prompt_int("Member ID: ")
    if book_id is None or member_id is None:
        raise LibraryError("IDs are whole numbers. Use options 5 and 6 to look them up.")
    title = borrow_book(book_id, member_id)
    print(f"'{title}' is now borrowed.")


def handle_return():
    book_id = prompt_int("Book ID: ")
    if book_id is None:
        raise LibraryError("IDs are whole numbers. Use option 7 to see borrowed books.")
    title = return_book(book_id)
    print(f"'{title}' has been returned.")


def handle_list_members():
    members = list_members()
    if not members:
        print("No registered members found.")
        return
    rows = [(m["id"], m["name"], m["email"]) for m in members]
    print(tabulate(rows, headers=["ID", "Name", "Email"], tablefmt="grid"))


def handle_list_borrowed():
    borrowed = list_borrowed_books()
    if not borrowed:
        print("No books are out right now.")
        return
    rows = [(b["id"], b["title"], b["name"], b["borrow_date"]) for b in borrowed]
    print(tabulate(rows, headers=["Book ID", "Title", "Borrowed by", "Since"], tablefmt="grid"))


def handle_search():
    term = prompt_input("Search title or author: ")
    show_books(search_books(term), f"No books match '{term}'.")


ACTIONS = {
    "1": handle_add_book,
    "2": handle_add_member,
    "3": handle_borrow,
    "4": handle_return,
    "5": lambda: show_books(list_books()),
    "6": handle_list_members,
    "7": handle_list_borrowed,
    "8": handle_search,
}


def main():
    initialize_database()
    while True:
        print(MENU)
        choice = prompt_input("Select an option: ")
        if choice == "0":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action is None:
            print("Invalid option. Please try again.")
            continue
        try:
            action()
        except LibraryError as error:
            print(f"Sorry: {error}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
