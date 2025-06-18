#!/usr/bin/python3
"""
This module demonstrates the use of class methods and static methods
within a Calculator class.
"""

class Calculator:
    """
    A simple calculator class to illustrate class and static methods.
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method to add two numbers.
        It does not have access to class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method to multiply two numbers.
        It has access to class-level attributes via the 'cls' parameter.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b