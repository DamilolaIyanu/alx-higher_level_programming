#!/usr/bin/python3
"""module for my list"""
class MyList(list):
    """the base class"""
    def print_sorted(self):
        """method for printing list"""
        print(sorted(self))
