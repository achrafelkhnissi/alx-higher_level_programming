#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Return a tuple with the length of a string and its first character.

    Args:
      sentence: The string.

    Returns:
      A tuple with 2 elements:
        The length of the string.
        The first character of the string.
    """
    length = len(sentence)
    first = sentence[0] if length > 0 else None
    return length, first
