#!/usr/bin/python3
"""module to say my name"""


def say_my_name(first_name, last_name=""):
    """prints my name
    Args:
        first_name: the firstname
        last_name: the last name
    Raises:
        TypeError: if first_name or last_name  is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/3-say_my_name.test")
