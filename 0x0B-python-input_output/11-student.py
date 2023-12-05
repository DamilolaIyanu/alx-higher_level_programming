#!/usr/bin/python3
"""Module for student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the dict of clas student"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        ddict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                ddict[key] = value
        return ddict
    def reload_from_json(self, json):
        """replaces the attributes of student"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
