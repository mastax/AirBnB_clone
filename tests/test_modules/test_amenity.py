#!/usr/bin/python3
"""Unittest For Amenity File: Class And Methods"""

import unittest
import pep8
from models.amenity import Amenity
from models import amenity


class TestBaseModelpep8(unittest.TestCase):
    """_Validate _pep8"""

    def test_pep8(self):
        """Test For Base File And test_base File pep8"""
        _style = pep8.StyleGuide(quiet=True)
        _amen_pep8 = "models/amenity.py"
        _test_amen_pep8 = "tests/test_models/test_amenity.py"
        _result = _style.check_files([_amen_pep8, _test_amen_pep8])
        self.assertEqual(_result.total_errors, 0)


class TestDocsBaseModel(unittest.TestCase):
    """Test Docstrings For Base And test_base Files"""

    def test_module(self):
        """Check Module Docstrings"""
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class(self):
        """Check Class Docstrings"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method(self):
        """Check Method Docstrings"""
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()