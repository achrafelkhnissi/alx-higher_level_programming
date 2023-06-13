#!/usr/bin/python3


"""
Module for from_json_string method.
"""


import json


def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string

    Arguments:
        my_str {str} -- [string to be converted]
    """
    return json.loads(my_str)
