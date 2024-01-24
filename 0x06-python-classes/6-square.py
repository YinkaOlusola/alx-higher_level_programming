#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (tuple): A tuple of two integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of size

        Args:
            value (int): The size of the new square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the positional value."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the positional value.

        Args:
            value (tuple): A tuple of two integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """Return the area of the square."""
        return (self.__size**2)


    def my_print(self):
        """Prints the square with character #."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print("")
