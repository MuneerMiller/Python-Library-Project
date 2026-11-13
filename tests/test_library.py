import os
import tempfile
import unittest

from utils import config


class LibraryTestCase(unittest.TestCase):
    """Each test gets its own empty database file."""

    def setUp(self):
        handle, self.db_path = tempfile.mkstemp(suffix=".db")
        os.close(handle)
        self.original_db = config.DB_NAME
        config.DB_NAME = self.db_path

        from init_db import initialize_database

        initialize_database()

    def tearDown(self):
        config.DB_NAME = self.original_db
        os.remove(self.db_path)


class BookTests(LibraryTestCase):
    def test_add_and_list_books(self):
        from models.book import add_book, list_books

        book_id = add_book("  Things Fall Apart ", "Chinua Achebe")
        books = list_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["id"], book_id)
        self.assertEqual(books[0]["title"], "Things Fall Apart")
        self.assertTrue(books[0]["available"])

    def test_book_needs_title_and_author(self):
        from models.book import add_book
        from models.errors import LibraryError

        with self.assertRaises(LibraryError):
            add_book("", "Someone")
        with self.assertRaises(LibraryError):
            add_book("A Title", "   ")

    def test_search_matches_title_or_author_ignoring_case(self):
        from models.book import add_book, search_books

        add_book("Long Walk to Freedom", "Nelson Mandela")
        add_book("Born a Crime", "Trevor Noah")
        self.assertEqual([b["title"] for b in search_books("freedom")], ["Long Walk to Freedom"])
        self.assertEqual([b["title"] for b in search_books("NOAH")], ["Born a Crime"])
        self.assertEqual(search_books("nothing like this"), [])


class MemberTests(LibraryTestCase):
    def test_register_member(self):
        from models.member import add_member, list_members

        member_id = add_member("Thandi", "Thandi@Example.com")
        members = list_members()
        self.assertEqual(members[0]["id"], member_id)
        self.assertEqual(members[0]["email"], "thandi@example.com")

    def test_duplicate_email_is_rejected(self):
        from models.errors import LibraryError
        from models.member import add_member

        add_member("Thandi", "thandi@example.com")
        with self.assertRaises(LibraryError):
            add_member("Someone else", "THANDI@example.com")

    def test_invalid_email_is_rejected(self):
        from models.errors import LibraryError
        from models.member import add_member

        with self.assertRaises(LibraryError):
            add_member("Thandi", "not-an-email")


class BorrowingTests(LibraryTestCase):
    def setUp(self):
        super().setUp()
        from models.book import add_book
        from models.member import add_member

        self.book_id = add_book("Cry, the Beloved Country", "Alan Paton")
        self.member_id = add_member("Sipho", "sipho@example.com")

    def test_borrow_and_return(self):
        from models.book import list_books
        from models.borrowing import borrow_book, list_borrowed_books, return_book

        borrow_book(self.book_id, self.member_id)
        self.assertFalse(list_books()[0]["available"])
        self.assertEqual(list_borrowed_books()[0]["name"], "Sipho")

        return_book(self.book_id)
        self.assertTrue(list_books()[0]["available"])
        self.assertEqual(list_borrowed_books(), [])

    def test_cannot_borrow_a_book_twice(self):
        from models.borrowing import borrow_book
        from models.errors import LibraryError

        borrow_book(self.book_id, self.member_id)
        with self.assertRaises(LibraryError):
            borrow_book(self.book_id, self.member_id)

    def test_unknown_book_or_member(self):
        from models.book import list_books
        from models.borrowing import borrow_book
        from models.errors import LibraryError

        with self.assertRaises(LibraryError):
            borrow_book(999, self.member_id)
        with self.assertRaises(LibraryError):
            borrow_book(self.book_id, 999)
        self.assertTrue(list_books()[0]["available"], "a failed borrow leaves the book available")

    def test_cannot_return_a_book_that_is_not_out(self):
        from models.borrowing import return_book
        from models.errors import LibraryError

        with self.assertRaises(LibraryError):
            return_book(self.book_id)


if __name__ == "__main__":
    unittest.main()
