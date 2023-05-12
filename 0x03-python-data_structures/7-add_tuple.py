#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
  Add 2 tuples.

  Args:
    tuple_a: The first tuple.
    tuple_b: The second tuple.

  Returns:
    A tuple with 2 integers:
      The first element should be the addition of the first element of each argument
      The second element should be the addition of the second element of each argument

  Raises:
    TypeError: If either tuple is not a tuple of integers.
  """

    if not isinstance(tuple_a, tuple) or not isinstance(tuple_b, tuple):
        raise TypeError("Both arguments must be tuples of integers")

    # Get the lengths of the tuples
    length_a = len(tuple_a)
    length_b = len(tuple_b)

    # If either tuple is shorter than 2, pad it with zeros
    if length_a < 2:
        tuple_a = tuple_a + (0,) * (2 - length_a)
    if length_b < 2:
        tuple_b = tuple_b + (0,) * (2 - length_b)

    # Add the tuples
    return tuple(x + y for x, y in zip(tuple_a, tuple_b))
