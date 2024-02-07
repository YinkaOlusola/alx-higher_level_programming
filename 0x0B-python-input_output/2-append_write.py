#!/usr/bin/python3
"""Defines a function that appends to a file."""


def append_write(filename="", text=""):
    """Appends text to filename.

    Args:
        filename (str): The name of the file to be appended.
        text (str): The text to be appended to the file.
    Returns:
        The number of characters appended to the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
