#!/usr/bin/python3


"""
Module for add_item method.
"""


import json


def add_item(args):
    """
    adds all arguments to a Python list, and then save them to a file

    Arguments:
        args {list} -- [list of arguments]
    """
    try:
        with open("add_item.json", mode="r", encoding="utf-8") as f:
            my_list = json.load(f)
    except FileNotFoundError:
        my_list = []
    for arg in args:
        my_list.append(arg)
    with open("add_item.json", mode="w", encoding="utf-8") as f:
        json.dump(my_list, f)
