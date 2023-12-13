#!/usr/bin/python3
"""Module for lockedclass"""


class LockedClass:
    """prevents the user dynamically creating new instance attributes"""
    __slots__ = ["first_name"]
