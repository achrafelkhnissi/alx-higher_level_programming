#!/usr/bin/python3

"""Module for LockedClass."""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.

    Attributes:
        first_name (str): first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self)
        """Initializes the instance.

        Args:
            first_name (str): The value for the 'first_name' attribute (default: "").
        """
        self.first_name = "first_name"