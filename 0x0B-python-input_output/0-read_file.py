#!/usr/bin/python3
"""A module that reads from a file"""


def read_file(filename=""):
    """Reads from a file and prints to the stdout"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
