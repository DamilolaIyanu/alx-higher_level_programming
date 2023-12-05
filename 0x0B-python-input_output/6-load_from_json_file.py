#!/usr/bin/python3
"""Module to load from json"""


import json


def load_from_json_file(filename):
    """loads from json file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
