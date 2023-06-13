#!/usr/bin/python3


"""
Module for append_write method.
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and returns the
    number of characters added

    Arguments:
        filename {str} -- [name of the file]
        text {str} -- [text to append]
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
