#!/usr/bin/python3
"""Defines a class called Base."""


class Base:
    """This is a Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Assigns the instance id.
        Args:
            id (int): The instance attribute id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
