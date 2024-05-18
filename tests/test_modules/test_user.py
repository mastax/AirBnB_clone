#!/usr/bin/python3
"""Unittest For User File: Class And Methods"""

import unittest
import pep8
from models.user import User
from models import user


class TestBaseModelpep8(unittest.TestCase):
    """ValIdate pep8"""

    def test_pep8(self):
        """Test For Base File And test_base File pep8"""
        _style = pep8.StyleGuide(quiet=True)
        _user_pep8 = "models/user.py"
        _test_user_pep8 = "tests/test_models/test_user.py"
        _result = _style.check_files([_user_pep8, _test_user_pep8])
        self.assertEqual(_result.total_errors, 0)


class TestDocsBaseModel(unittest.TestCase):
    """Test Docstrings For Base And test_base Files"""

    def test_module(self):
        """Check Module Docstrings"""
        self.assertTrue(len(user.__doc__) > 0)

    def test_class(self):
        """Check Class Docstrings"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for _func in dir(User):
            self.assertTrue(len(_func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
