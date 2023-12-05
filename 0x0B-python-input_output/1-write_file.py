#!/usr/bin/python3
"""Module to write a string to a textfile"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
