#!/usr/bin/python3
"""Module to write using json"""


import json


def save_to_json_file(my_obj, filename):
    """writes to json file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
