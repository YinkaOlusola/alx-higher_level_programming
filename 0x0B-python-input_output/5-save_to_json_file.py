#!/usr/bin/python3
"""Defines a function that saves an object to a file."""
import json


def save_to_json(my_obj, filename):
    """Writes an object to a text file using JSON
        representation.

        Args:
            my_obj: Object to be written to a text file in JSON format
            filename: The file to write to.
        Returns:
            The number of characters written to the file.
        """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
