#!/usr/bin/python3
"""
This module demonstrates inheritance and composition by modeling a library system.
"""

class Book:
    """
    Base class for a book.
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

    def __str__(self):
        """
        Returns a string representation for a generic book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    A derived class for an electronic book, inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes an EBook instance.

        Args:
            title (str): The title of the ebook.
            author (str): The author of the ebook.
            file_size (int): The file size of the ebook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size
        
    def __str__(self):
        """
        Returns a string representation for an EBook.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    A derived class for a printed book, inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation for a PrintBook.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    A class representing a library, which is composed of books.
    """
    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook) to the library's collection.

        Args:
            book (Book): The book instance to add.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of each book in the library's collection.
        """
        for book in self.books:
            print(book)