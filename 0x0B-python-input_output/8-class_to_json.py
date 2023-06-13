#!/usr/bin/python3


"""
Module for class_to_json method.
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object

    Arguments:
        obj {object} -- [object to serialize]
    """

    return obj.__dict__
