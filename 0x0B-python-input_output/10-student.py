#!/usr/bin/python3
""" a class that defines a student based on 9-student.py"""


class Student:
    """ A Student class """
    def __init__(self, first_name, last_name, age):
        """ the instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ a json function that retrieves a dic.. rep of student """
        if type(attrs) == list and all(type(item) == str for item in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
