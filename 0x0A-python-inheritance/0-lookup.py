#!/usr/bin/python3

"""Defines an object that returns a list of 
available attributes and methods of an object
"""

def lookup(obj):
    """Returns a list of available attributes and methods"""
    return (dir(obj))
