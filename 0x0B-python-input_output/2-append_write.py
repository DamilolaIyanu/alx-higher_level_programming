#!/usr/bin/python3
"""Module to write a string to a textfile"""


def append_write(filename="", text=""):
    """appends a string to a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
