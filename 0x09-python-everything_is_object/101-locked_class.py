#!/usr/bin/python3
"""Module for lockedclass"""


class LockedClass:
    """prevents the user dynamically creating new instance attributes"""
    __slot__ = ["first_name"]
