#!/usr/bin/python3
"""Unittest For State File: Class And Methods"""

import unittest
import pep8
from models.state import State
from models import state


class TestBaseModelpep8(unittest.TestCase):
    """ValIdate pep8"""

    def test_pep8(self):
        """Test For Base File And test_base File pep8"""
        _style = pep8.StyleGuide(quiet=True)
        _state_pep8 = "models/state.py"
        _test_state_pep8 = "tests/test_models/test_state.py"
        _result = _style.check_files([_state_pep8, _test_state_pep8])
        self.assertEqual(_result.total_errors, 2)


class TestDocsBaseModel(unittest.TestCase):
    """Test Docstrings For Base And test_base Files"""

    def test_module(self):
        """Check Module Docstrings"""
        self.assertTrue(len(state.__doc__) > 0)

    def test_class(self):
        """Check Class Docstrings"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_method(self):
        """Check Method Docstrings"""
        for _func in dir(State):
            self.assertTrue(len(_func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
