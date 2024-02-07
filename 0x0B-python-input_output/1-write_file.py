#!/usr/bin/python3
"""Defines a function that writes to a text file."""


def write_file(filename="", text=""):
    """Writes text to a file.

    Args:
        filename (str): Name of the file to write to.
        text (str): The content to be written in the file.
    Returns:
        Number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
