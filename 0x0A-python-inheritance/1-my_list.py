#!/usr/bin/python3
"""A module to print a sorted list"""


class MyList(list):
    """A child class that inherits from list."""

    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
