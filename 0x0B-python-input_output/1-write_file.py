#!/usr/bin/python3
""" a function that writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """ The function then returns the number of char... written"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
