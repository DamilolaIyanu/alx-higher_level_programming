#!/usr/bin/python3
"""This module adds integer"""


def add_integer(a, b=98):
    """Adds two integers
        Args:
            a: the first integer
            b: the second integer with default value 98
        Raises:
            TypeError: if a or b is not integers or float
        Return:
            The sum of the integers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/0-add_integer.txt")
