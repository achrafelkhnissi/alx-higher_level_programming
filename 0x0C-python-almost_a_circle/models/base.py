#!/usr/bin/python3


"""
Base class for all other classes in this project
"""


class Base:
    """
    Base class for all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
