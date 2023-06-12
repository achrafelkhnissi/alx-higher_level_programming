#!/usr/bin/python3

"""Module for my_list class"""


class MyList(list):
    """Class that inherits from list"""
    pass

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
