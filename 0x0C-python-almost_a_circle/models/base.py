#!/usr/bin/python3

"""
Base class for all other classes in this project
"""

import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert list_dictionaries to JSON string

        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write JSON string representation of list_objs to a file
        args:
            list_objs (list): list of instances that inherit from Base
        """

        filename = cls.__name__ + ".json"  # Generate the filename based on the class name
        json_string = cls.to_json_string(list_objs)  # Convert list_objs to JSON string

        with open(filename, "w") as file:
            file.write(json_string)
