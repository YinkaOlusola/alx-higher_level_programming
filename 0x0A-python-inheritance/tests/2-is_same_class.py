#!/usr/bin/python3
""" A function to check if an object belongs to a class"""


def is_same_class(obj, a_class):
    """ A function to check if am object is an instance of a class.

    Args:
        obj (object): The object to be checked if it's an instance of a class.
        a_class: The class against which object is checked.

    Return:
        True if obj is an instance of a_class and False otherwise.
    """

    return (isinstance(obj, a_class))


