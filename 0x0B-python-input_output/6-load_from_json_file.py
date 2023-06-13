#!/usr/bin/python3


"""
Module for load_from_json_file method.
"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Arguments:
        filename {str} -- [name of the file]

    Returns:
        [object] -- [Object from a “JSON file”]
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
