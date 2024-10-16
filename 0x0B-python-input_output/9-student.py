#!/usr/bin/python3
""" a class that defines a student"""


class Student:
    """ A Student class """
    def __init__(self, first_name, last_name, age):
        """ the instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ a json function that retrieves a dic.. rep of student """
        return self.__dict__
