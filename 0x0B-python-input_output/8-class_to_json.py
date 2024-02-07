#!/usr/bin/python3
"""Defines a Class-to-JSON function"""
import json


def class_to_json(obj):
    """A function that returns the dictionary description"""
    return (obj.__dict__)
