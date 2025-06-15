class Book:
    """
    Represents a book with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False # Already checked out

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False # Was not checked out

    def is_available(self):
        """Checks if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the Book."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of books in a library.
    """
    def __init__(self):
        """Initializes the Library with an empty list of books."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Adds a Book instance to the library's collection.

        Args:
            book (Book): The Book instance to add.
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Invalid object. Only Book instances can be added.")

    def check_out_book(self, title):
        """
        Checks out a book by its title.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"Checked out '{title}'.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book with title '{title}' not found in the library.")

    def return_book(self, title):
        """
        Returns a book by its title.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title:
                if not book.is_available(): # If it's checked out
                    book.return_book()
                    print(f"Returned '{title}'.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book with title '{title}' not found in the library.")

    def list_available_books(self):
        """
        Lists all books in the library that are currently available.
        """
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available.")
            return

        for book in available_books:
            print(book) # Uses the __str__ method of the Book class