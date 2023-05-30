#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    """
    Class that defines a square

    Attributes:
        size (int): size of the square
    """
    def __init__(self, size=0):
        """
        Init method is a constructor for Square class
        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
