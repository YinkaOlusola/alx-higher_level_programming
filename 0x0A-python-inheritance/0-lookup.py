#!/usr/bin/python3
"""Defines an object function to return attributes"""


def lookup(obj):
    """Returns a list of object attributes and methods"""
    return (dir(obj))
