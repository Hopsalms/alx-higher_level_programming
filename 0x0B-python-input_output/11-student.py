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
        if type(attrs) is list and all(type(item) is str for item in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ a public method that replaces all attributes of d stud.."""
        for key, value in json.items():
            setattr(self, key, value)
