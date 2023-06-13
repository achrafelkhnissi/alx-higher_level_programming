#!/usr/bin/python3


"""
Module for save_to_json_file method.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    Arguments:
        my_obj {object} -- [object to be converted]
        filename {str} -- [name of the file]
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
