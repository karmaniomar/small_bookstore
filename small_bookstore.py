# =============================================================================
# Project: Bookstore Management System
# Author: Omar Karmani
# Purpose: A simple command-line program to manage a bookstore database
# Description: This program allows the user to add, update, delete, search, and
# display books in a SQLite database.
# =============================================================================

import sqlite3


class BookstoreDB:
    def __init__(self, db_name="small_bookstore_stock.db"):
        self.db_name = db_name
        self.initialise_database()

    def initialise_database(self):
        """Initialise the database and create the 'book' table if it does not exist."""
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS book (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL UNIQUE,
                        author TEXT NOT NULL,
                        qty INTEGER NOT NULL
                    )
                """)
                books = [
                    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
                    (
                        3002,
                        "Harry Potter and the Philosopher's Stone",
                        "J.K. Rowling",
                        40,
                    ),
                    (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
                    (3004, "The Lord of the Rings", "J.R.R. Tolkien", 37),
                    (3005, "Alice in Wonderland", "Lewis Carroll", 12),
                ]
                cursor.executemany(
                    "INSERT OR IGNORE INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)",
                    books,
                )
                connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def display_books(self):
        """Display all books in the database."""
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM book")
                books = cursor.fetchall()
                if books:
                    print("\nAll Books in Database:")
                    for book in books:
                        print(
                            f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}"
                        )
                else:
                    print("No books found in the database.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def book_id_exists(self, book_id):
        """Check if a book ID exists in the database."""
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT id FROM book WHERE id = ?", (book_id,))
                return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    def add_book(self, book_id, title, author, qty):
        """Add a new book to the database."""
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)",
                    (book_id, title, author, qty),
                )
                connection.commit()
                print("Book added successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def update_book(self, book_id, title, author, qty):
        """Update an existing book in the database."""
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?",
                    (title, author, qty, book_id),
                )
                connection.commit()
                print("Book updated successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def delete_book(self, book_id):
        """Delete a book from the database."""
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))
                connection.commit()
                print("Book deleted successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def search_books(self, search_term):
        """Search for books in the database."""
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT * FROM book WHERE id LIKE ? OR title LIKE ? OR author LIKE ?",
                    (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"),
                )
                books = cursor.fetchall()
                return books
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []


class BookstoreCLI:
    def __init__(self):
        self.db = BookstoreDB()

    def validate_quantity_input(self, prompt):
        """Validate quantity input (digits only)."""
        while True:
            try:
                quantity = input(
                    f'{prompt} (enter "back" to return to the menu): '
                ).strip()
                if quantity.lower() == "back":
                    return "back"
                if quantity.isdigit():
                    return int(quantity)
                else:
                    print("Error: Quantity must be a number. Please try again.")
            except Exception as e:
                print(f"Unexpected error: {e}")

    def validate_non_empty_input(self, prompt, field_name):
        """Validate non-empty input."""
        while True:
            try:
                user_input = input(
                    f'{prompt} (enter "back" to return to the menu): '
                ).strip()
                if user_input.lower() == "back":
                    return "back"
                if user_input:
                    return user_input
                else:
                    print(f"Error: {field_name} cannot be empty. Please try again.")
            except Exception as e:
                print(f"Unexpected error: {e}")

    def enter_book(self):
        """Add a new book to the database."""
        try:
            self.db.display_books()
            while True:
                book_id = self.validate_non_empty_input("Enter book ID", "Book ID")
                if book_id == "back":
                    return
                if not book_id.isdigit():
                    print("Error: Book ID must be a number. Please try again.")
                    continue
                book_id = int(book_id)
                if self.db.book_id_exists(book_id):
                    print(
                        "Error: A book with this ID already exists. Please enter a new ID."
                    )
                else:
                    break

            title = self.validate_non_empty_input("Enter book title", "Title")
            if title == "back":
                return
            author = self.validate_non_empty_input("Enter book author", "Author")
            if author == "back":
                return
            qty = self.validate_quantity_input("Enter quantity")
            if qty == "back":
                return

            self.db.add_book(book_id, title, author, qty)
        except Exception as e:
            print(f"Unexpected error: {e}")

    def update_book(self):
        """Update an existing book in the database."""
        try:
            self.db.display_books()
            book_id = self.validate_non_empty_input(
                "Enter book ID to update", "Book ID"
            )
            if book_id == "back":
                return
            if not book_id.isdigit():
                print("Error: Book ID must be a number. Please try again.")
                return
            book_id = int(book_id)
            if not self.db.book_id_exists(book_id):
                print("Error: No book with this ID exists. Please try again.")
                return

            title = self.validate_non_empty_input("Enter new book title", "Title")
            if title == "back":
                return
            author = self.validate_non_empty_input("Enter new book author", "Author")
            if author == "back":
                return
            qty = self.validate_quantity_input("Enter new quantity")
            if qty == "back":
                return

            self.db.update_book(book_id, title, author, qty)
            print("Book updated successfully.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def delete_book(self):
        """Delete a book from the database."""
        try:
            self.db.display_books()
            book_id = self.validate_non_empty_input(
                "Enter book ID to delete", "Book ID"
            )
            if book_id == "back":
                return
            if not book_id.isdigit():
                print("Error: Book ID must be a number. Please try again.")
                return
            book_id = int(book_id)
            if not self.db.book_id_exists(book_id):
                print("Error: No book with this ID exists. Please try again.")
                return

            self.db.delete_book(book_id)
            print("Book deleted successfully.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def search_books(self):
        """Search for books in the database."""
        try:
            search_term = self.validate_non_empty_input(
                "Enter search term (title or author)", "Search term"
            )
            if search_term == "back":
                return

            books = self.db.search_books(search_term)
            if books:
                print("\nSearch Results:")
                for book in books:
                    print(
                        f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}"
                    )
            else:
                print("No books found matching the search term.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def run_program(self):
        """Display the menu and handle user input."""
        try:
            while True:
                print("\nBookstore Management System")
                print("1. Enter book")
                print("2. Update book")
                print("3. Delete book")
                print("4. Search books")
                print("5. Show all books")
                print("0. Exit")
                choice = input("Enter your choice: ").strip()
                if choice == "1":
                    self.enter_book()
                elif choice == "2":
                    self.update_book()
                elif choice == "3":
                    self.delete_book()
                elif choice == "4":
                    self.search_books()
                elif choice == "5":
                    self.db.display_books()
                elif choice == "0":
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    cli = BookstoreCLI()
    cli.run_program()
