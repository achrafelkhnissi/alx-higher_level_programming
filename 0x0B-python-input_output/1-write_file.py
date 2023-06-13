#!/usr/bin/python3


"""
Module for write_file method.
"""


def write_file(filename="", text=""):
    """
    Method for write_file.

    Args:
        filename (str): The file name.
        text (str): The text to write.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
