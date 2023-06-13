#!/usr/bin/python3


"""
Module for read_file method.
"""


def read_file(filename=""):
    """
    Method for read_file.

    Args:
        filename (str): The file name.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
