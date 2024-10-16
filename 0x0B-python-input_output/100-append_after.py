#!/usr/bin/python3
""" a function that inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ after each line containing a specific string (see example): """
    text = ""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        for line in a_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode='w', encoding='utf-8') as new_file:
        new_file.write(text)
