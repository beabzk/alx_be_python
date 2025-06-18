#!/usr/bin/python3
"""
This module defines the Book class with magic methods.
"""

class Book:
    """
    A class to represent a book with title, author, and year.
    It demonstrates the use of __init__, __del__, __str__, and __repr__ magic methods.
    """
    def __init__(self, title, author, year):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Prints a message upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns an informal, user-friendly string representation of the Book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation that can recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"