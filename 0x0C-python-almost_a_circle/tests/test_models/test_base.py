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

    def test_to_json_string_with_none(self):
        """Test to_json_string with None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_with_empty_list(self):
        """Test to_json_string with empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_one_dictionary(self):
        """Test to_json_string with one dictionary"""
        self.assertEqual(Base.to_json_string([{"id": 12}]), '[{"id": 12}]')

    def test_to_json_string_with_two_dictionaries(self):
        """Test to_json_string with two dictionaries"""
        self.assertEqual(Base.to_json_string([{"id": 12}, {"id": 13}]),
                         '[{"id": 12}, {"id": 13}]')

    def test_to_json_string_with_more_args(self):
        """Test to_json_string with more args"""
        with self.assertRaises(TypeError):
            Base.to_json_string([{"id": 12}, {"id": 13}], 1)

    def test_to_json_string_with_no_args(self):
        """Test to_json_string with no args"""
        with self.assertRaises(TypeError):
            Base.to_json_string()


if "__main__" == __name__:
    unittest.main()
