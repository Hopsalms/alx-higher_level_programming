#!/usr/bin/python3
""" a function that returns the dictionary description """


def class_to_json(obj):
    """ return the dictionary with simple data struct """
    return obj.__dict__
