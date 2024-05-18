#!/usr/bin/python3
"""Unittest For Place File: Class And Methods"""

import unittest
import pep8
from models.place import Place
from models import place


class TestBaseModelpep8(unittest.TestCase):
    """ValIdate pep8"""

    def test_pep8(self):
        """Test For Base File And test_base File pep8"""
        _style = pep8.StyleGuide(quiet=True)
        _place_pep8 = "models/place.py"
        _test_place_pep8 = "tests/test_models/test_place.py"
        _result = _style.check_files([_place_pep8, _test_place_pep8])
        self.assertEqual(_result.total_errors, 2)


class TestDocsBaseModel(unittest.TestCase):
    """Test Docstrings For Base And test_base Files"""

    def test_module(self):
        """Check Module Docstrings"""
        self.assertTrue(len(place.__doc__) > 0)

    def test_class(self):
        """Check Class Docstrings"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_method(self):
        """Check Method Docstrings"""
        for _func in dir(Place):
            self.assertTrue(len(_func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
