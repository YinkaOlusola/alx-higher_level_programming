#!/usr/bin/python3
"""Defines a function that returns JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Converts a string to JSON format.

    Args:
        my_obj: The object to be serialized.
    Returns:
        The JSON representation of an object.
    """
    return json.dumps(my_obj)
