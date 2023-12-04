#!/usr/bin/python3
"""Module for lookup"""


def lookup(obj):
    """looks objects and attributes.
    Args:
        obj: the object to list

    Return:
        list: the list of attribute
    """
    return dir(obj)
