#!/usr/bin/python3


"""
Module for to_json_string method.
"""


import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    Arguments:
        my_obj {object} -- [object to be converted]
    """
    return json.dumps(my_obj)
