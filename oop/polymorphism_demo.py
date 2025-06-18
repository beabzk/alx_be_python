#!/usr/bin/python3
"""
This module demonstrates polymorphism with a Shape base class
and derived Rectangle and Circle classes.
"""

import math

class Shape:
    """
    A base class for geometric shapes.
    """
    def area(self):
        """
        Calculates the area of the shape. This method should be
        overridden by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this!")

class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.
    """
    def __init__(self, length, width):
        """
        Initializes a Rectangle instance.

        Args:
            length (float or int): The length of the rectangle.
            width (float or int): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        """
        Initializes a Circle instance.

        Args:
            radius (float or int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)