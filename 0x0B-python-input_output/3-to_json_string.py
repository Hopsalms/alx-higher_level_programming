#!/usr/bin/python3
"""  a function that returns the JSON representation of an object str """
import json
""" this will enable us use the json module """


def to_json_string(my_obj):
    """ The function """
    return json.dumps(my_obj)
