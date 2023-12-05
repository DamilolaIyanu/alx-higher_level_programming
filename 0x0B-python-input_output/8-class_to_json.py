#!/usr/bin/python3
"""MOdule for json dictionary"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return obj.__dict__
