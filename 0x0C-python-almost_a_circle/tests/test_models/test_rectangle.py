#!/usr/bin/python3

"""Unittest for rectangle.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_init_with_id(self):
        """Test __init__ with id"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)

    def test_init_without_id(self):
        """Test __init__ without id"""
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, 1)

    def test_init_with_string(self):
        """Test __init__ with string"""
        r3 = Rectangle(10, 2, 0, 0, "hello")
        self.assertEqual(r3.id, "hello")

    def test_init_with_float(self):
        """Test __init__ with float"""
        r4 = Rectangle(10, 2, 0, 0, 3.14)
        self.assertEqual(r4.id, 3.14)


if __name__ == "__main__":
    unittest.main()
