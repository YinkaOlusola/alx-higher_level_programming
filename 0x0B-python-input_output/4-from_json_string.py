#!/usr/bin/python3
"""Defines a function that convert an object to a JSON string."""
import json


def from_json_string(my_str):
    """Converts JSON to Python object.

    Args:
        my_str (str): json to be converted to string
    Returns:
        An object represented by a JSON string.
    """
    return json.load(my_str)
