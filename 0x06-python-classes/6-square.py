#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    """
    Class that defines a square

    Attributes:
        size (int): size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Init method is a constructor for Square class
        Args:
            size: size of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Public instance method that returns the current square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Public instance method that returns the current square size
        Args:
            value: size of the square

        Returns:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Public instance method that returns the current square position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Public instance method that returns the current square position
        Args:
            value: position of the square

        Returns:
            TypeError: if position is not an integer
            ValueError: if position is less than 0
        """
        if (isinstance(value, tuple) is False) or (len(value) != 2) or \
                (isinstance(value[0], int) is False) or \
                (isinstance(value[1], int) is False) or \
                (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Public instance method that returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public instance method that prints in stdout the square with the
        character #, while printing spaces for the position of the square
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

