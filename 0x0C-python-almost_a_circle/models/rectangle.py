#!/usr/bin/python3

"""
Module for Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x position of rectangle
            y (int): y position of rectangle
            id (int): id of rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for width

        Returns:
            width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width

        Args:
            value (int): width of rectangle
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter for height

        Returns:
            height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height

        Args:
            value (int): height of rectangle
        """
        self.__height = value
