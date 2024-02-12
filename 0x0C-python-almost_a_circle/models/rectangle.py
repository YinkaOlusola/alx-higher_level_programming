#!/usr/bin/python3
"""Defines a Rectangle Class."""

from models.base import Base

class Rectangle(Base):
    """A Rectangle class that inherits from the Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the new rectangle
            y (int): The y coordinate of the new rectangle.
            id (int): Unique identifier
        Raise:
            TypeError: If either of height or width is not an integer
            ValueError: If either of height or width is <= 0
            TypeError: If either of x or y is not an integer
            ValueError: If either of x or y is less than zero
            """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    
    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Sets/gets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the rectangle."""
        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        for i in range(self.__height):
            [print("#", end="") for j in range(self.__width)]
            print("")
