#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    """Square class with a private instance attribute"""

    def __init__(self, size=0):
        """Initializes the data"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
