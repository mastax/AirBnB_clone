#!/usr/bin/python3
"""Unittest For Review File: Class And Methods"""

import unittest
import pep8
from models.review import Review
from models import review


class TestBaseModelpep8(unittest.TestCase):
    """ValIdate pep8"""

    def test_pep8(self):
        """Test For Base File And test_base File pep8"""
        _style = pep8.StyleGuide(quiet=True)
        _review_pep8 = "models/review.py"
        _test_review_pep8 = "tests/test_models/test_review.py"
        _result = _style.check_files([_review_pep8, _test_review_pep8])
        self.assertEqual(_result.total_errors, 2)


class TestDocsBaseModel(unittest.TestCase):
    """Test Docstrings For Base And test_base Files"""

    def test_module(self):
        """Check module Docstrings"""
        self.assertTrue(len(review.__doc__) > 0)

    def test_class(self):
        """Check Class Docstrings"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_method(self):
        """Check Method Docstrings"""
        for _func in dir(Review):
            self.assertTrue(len(_func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
