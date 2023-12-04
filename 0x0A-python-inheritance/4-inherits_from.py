#!/usr/bin/python3
"""Module to check for inheritance directly or indirectly"""


def inherits_from(obj, a_class):
    """Checks if object is an instance of a class directly or not"""
    return isinstance(obj, a_class) and type(obj) != a_class
