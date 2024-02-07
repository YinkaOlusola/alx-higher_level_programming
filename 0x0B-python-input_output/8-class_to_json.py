#!/usr/bin/python3
import json


def class_to_jason(obj):
    """A function that returns the dictionary description"""
    return (json.dumps(obj.__class__.__doc__))
