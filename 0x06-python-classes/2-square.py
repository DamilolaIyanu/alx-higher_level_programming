#!/usr/bin/python3
"""An empty class module."""


class Square:
    """Defines the class Square."""
    def __init__(self, size=0):
        """Initializer

        arguments:
            size: the side of a square
        raise:
            TypeError: size is not a digit
            ValueError: size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
