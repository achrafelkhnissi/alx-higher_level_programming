#!/usr/bin/python3


"""
Module for add_item method.
"""


import sys


load_from_json_file = __import__('6-load_from_json_file') \
    .load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item(args):
    """
    adds all arguments to a Python list, and then save them to a file

    Arguments:
        args {list} -- [list of arguments]
    """

    filename = "add_item.json"

    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    for i in range(1, len(args)):
        my_list.append(args[i])
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_item(sys.argv)
