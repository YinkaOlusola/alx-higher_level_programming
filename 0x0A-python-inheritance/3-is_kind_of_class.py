#!/usr/bin/python3
"""Checks if an object is an instance of class or its Parent class"""


def is_kind_of_class(obj, a_class):
    """Returns True or False if obj is an instance of is_class.

    Args:
        obj (object): The object whose instances is to be checked.
        a_class (object): The class to check obj against
    Returns:
        True if obj is an instance of a_class or its derive.
        otherwise - False.
    """
    return (isinstance(obj, a_class))
