#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Find the biggest integer of a list.

    Args:
      my_list: The list to be searched.

    Returns:
      The maximum integer in the list.

    Raises:
      TypeError: If the list is not a list of integers.
      ValueError: If the list is empty.
    """
    if not isinstance(my_list, list) or len(my_list) == 0:
        raise TypeError("my_list must be a list")

    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max
