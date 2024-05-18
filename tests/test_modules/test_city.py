#!/usr/bin/python3
"""Unittest For Test File: Class And Methods"""

import unittest
import pep8
from models.city import City
from models import city


class TestBaseModelpep8(unittest.TestCase):
    """ValIdate pep8"""

    def test_pep8(self):
        """Test For Base File And test_base File pep8"""
        _style = pep8.StyleGuide(quiet=True)
        _city_pep8 = "models/city.py"
        _test_city_pep8 = "tests/test_models/test_city.py"
        _result = _style.check_files([_city_pep8, _test_city_pep8])
        self.assertEqual(_result.total_errors, 2)


class TestDocsBaseModel(unittest.TestCase):
    """Test Docstrings For Base And test_base Files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(city.__doc__) > 0)

    def test_class(self):
        """Check Class Docstrings"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_method(self):
        """Check Method Docstrings"""
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
