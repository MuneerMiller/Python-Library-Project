from models.book import add_book, list_books
from models.member import add_member
from models.borrowing import borrow_book, return_book
from utils.helpers import prompt_input

def menu():
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Register a Member")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. List All Books")
    print("6. Exit")

    choice = prompt_input("Select an option: ")
    return choice

def main():
    while True:
        choice = menu()
        if choice == "1":
            title = prompt_input("Enter book title: ")
            author = prompt_input("Enter book author: ")
            add_book(title, author)
            print("Book added successfully!")
        elif choice == "2":
            name = prompt_input("Enter member name: ")
            email = prompt_input("Enter member email: ")
            add_member(name, email)
            print("Member registered successfully!")
        elif choice == "3":
            book_id = prompt_input("Enter book ID: ")
            member_id = prompt_input("Enter member ID: ")
            try:
                borrow_book(book_id, member_id)
                print("Book borrowed successfully!")
            except Exception as e:
                print(e)
        elif choice == "4":
            book_id = prompt_input("Enter book ID: ")
            return_book(book_id)
            print("Book returned successfully!")
        elif choice == "5":
            books = list_books()
            for book in books:
                print(book)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
