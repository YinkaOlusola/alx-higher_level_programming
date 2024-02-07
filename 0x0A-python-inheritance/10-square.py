#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class."""

    def __init__(self, size):
        """Instantiation function.
        Args:
            size : Length of a side of the rectangle.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
