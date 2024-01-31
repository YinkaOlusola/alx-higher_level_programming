#!/usr/bin/python3
"""A locked class."""


class LockedClass:
    """
    Prevent the user from dynamically creating a new instance
    attributes except when called 'first_name'.
    """

    __slots__ = ["first_name"]
