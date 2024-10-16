#!/usr/bin/python3
""" load from json file"""
import json
""" this is done becaasue the json module will be used"""


def load_from_json_file(filename):
    """ a function that creates an obj file from json"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        return json.load(a_file)
