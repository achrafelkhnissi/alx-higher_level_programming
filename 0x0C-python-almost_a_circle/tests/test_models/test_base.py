#!/usr/bin/python3

"""Unittest for base.py"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_init_with_id(self):
        """Test __init__ with id"""
        b1 = Base(id=12)
        self.assertEqual(b1.id, 12)

    def test_init_without_id(self):
        """Test __init__ without id"""
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_init_with_string(self):
        """Test __init__ with string"""
        b3 = Base("hello")
        self.assertEqual(b3.id, "hello")

    def test_init_with_float(self):
        """Test __init__ with float"""
        b4 = Base(3.14)
        self.assertEqual(b4.id, 3.14)
