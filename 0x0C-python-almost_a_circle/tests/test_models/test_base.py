#!/usr/bin/python3

"""Unittest for base.py"""


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_save_to_file_with_none(self):
        """Test save_to_file with None"""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_empty_list(self):
        """Test save_to_file with empty list"""
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_one_dictionary(self):
        """Test save_to_file with one dictionary"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        a_dict = [r1.to_dictionary()]
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            list_dict = json.loads(file.read())
        self.assertTrue(a_dict == list_dict)

    #
    # def test_save_to_file_with_two_dictionaries(self):
    #     """Test save_to_file with two dictionaries"""
    #     Base.save_to_file([{"id": 12}, {"id": 13}])
    #     with open("Base.json", "r") as f:
    #         self.assertEqual(f.read(), '[{"id": 12}, {"id": 13}]')
    #
    # def test_save_to_file_with_more_args(self):
    #     """Test save_to_file with more args"""
    #     with self.assertRaises(TypeError):
    #         Base.save_to_file([{"id": 12}, {"id": 13}], 1)
    #
    # def test_save_to_file_with_no_args(self):
    #     """Test save_to_file with no args"""
    #     with self.assertRaises(TypeError):
    #         Base.save_to_file()


if "__main__" == __name__:
    unittest.main()
