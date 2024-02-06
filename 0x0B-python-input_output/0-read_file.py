#!/usr/bin/python3
"""A module that reads from a file"""

def read_file(filename=""):
    """Reads from a file
    Args:
        filename (str): The name of the file to be read
    """
    with open(filename, encoding='utf-8') as f:
        read_data = f.read()
