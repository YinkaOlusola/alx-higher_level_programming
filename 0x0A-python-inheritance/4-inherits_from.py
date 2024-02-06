#!/usr/bin/python3
"""Checks if an object is an instance of an inherited class"""


def inherits_from(obj, a_class):
    """Returns True or False if obj is an instance of derived
    class of is_class.

    Args:
        obj (object): The object whose instances is to be checked.
        a_class (object): The parent class to check obj against
    Returns:
        True if obj is an instance of a_class or its derive.
        otherwise - False.
    """
    return ((issubclass(type(obj), a_class)) and (type(obj) != a_class))
