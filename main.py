from models.book import add_book, list_books
from models.member import add_member
from models.borrowing import borrow_book, return_book
from utils.helpers import prompt_input
from models.member import list_members
from tabulate import tabulate

def menu():
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Register a Member")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. List All Books")
    print("6. List Registered Members")
    print("7. Exit")
    choice = input("Select an option: ").strip()  # Remove whitespace and trailing characters
    return choice



def main():
    while True:
        choice = menu()
        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            add_book(title, author)
            print("Book added successfully!")
        elif choice == "2":
            name = input("Enter member name: ").strip()
            email = input("Enter member email: ").strip()
            success, message = add_member(name, email)  # Get status and message
            print(message)  # Display the message only once
        elif choice == "3":
            try:
                book_id = int(input("Enter book ID: ").strip())
                member_id = int(input("Enter member ID: ").strip())
                borrow_book(book_id, member_id)
                print("Book borrowed successfully!")
            except ValueError:
                print("Invalid input. Please enter numeric IDs.")
            except Exception as e:
                print(e)

        elif choice == "4":
            book_id = input("Enter book ID: ").strip()
            return_book(book_id)
            print("Book returned successfully!")
        elif choice == "5":
            books = list_books()
            if books:
                formatted_books = [(book[1], book[2]) for book in books]
                print("\nList of Books:")
                print(tabulate(formatted_books, headers=["Title", "Author"], tablefmt="grid"))
            else:
                print("No books found.")
        elif choice == "6":  # Correctly handle listing members
            members = list_members()
            if members:
                # Format members into a table-like format
                formatted_members = [(member[1], member[2]) for member in members]
                print("\nList of Registered Members:")
                print(tabulate(formatted_members, headers=["Name", "Email"], tablefmt="grid"))
            else:
                print("No registered members found.")
        elif choice == "7":  # Correctly handle exit
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")




if __name__ == "__main__":
    main()
