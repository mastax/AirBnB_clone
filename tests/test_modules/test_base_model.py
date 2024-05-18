#!/usr/bin/python3
"""Unittest For Basemodel File: Class And Methods"""

import os
import pep8
import unittest
from models.user import User
from models import base_model
from datetime import datetime
from models.base_model import BaseModel


class Test_Base_Model_outputs(unittest.TestCase):
    """Test_Base_outputs Test For Base Class"""

    def test_unique_id(self):
        """
        test_unique_id Method That Test If Id Is Unique
        """
        _instance1 = BaseModel()
        _instance2 = BaseModel()
        self.assertNotEqual(_instance1, _instance2)

    def test_id_type(self):
        """
        test_id_type Method That Test If Type Of Id Is Correct
        """
        _instance1 = BaseModel()
        self.assertEqual('<class \'str\'>', str(type(_instance1.id)))

    def test_exec_file(self):
        """
        test_exec_file Method To Test If File Has Read, Write And Exec
        Permissions
        """
        _read = os.access('models/base_model.py', os.R_OK)
        self.assertEqual(True, _read)
        _write = os.access('models/base_model.py', os.W_OK)
        self.assertEqual(True, _write)
        _exec = os.access('models/base_model.py', os.X_OK)
        self.assertEqual(True, _exec)

    def test_save(self):
        """
        test_save Method To Test If Each Time that The Instance Is
        Saved The update_at Attribute Is Updated
        """
        instance1 = BaseModel()
        _attr_updated_before_save = instance1.updated_at
        instance1.save()
        _attr_updated_after_save = instance1.updated_at
        self.assertNotEqual(_attr_updated_before_save, _attr_updated_after_save)

    def test_to_dict(self):
        """
        test_to_dict Method That Test If A Dictionary Is Returned
        And If updated_at And created_at Attributes Are In The Correct
        Format
        """
        _instance1 = BaseModel()
        _instance1_User = User()
        # test type of return
        self.assertEqual('<class \'dict\'>', str(type(_instance1.to_dict())))

        _updated_expected_format = _instance1.updated_at.isoformat()
        _created_expected_format = _instance1.created_at.isoformat()
        _class_attr_value_expected = type(_instance1_User).__name__
        _updated_actual_format = _instance1.to_dict()["updated_at"]
        _created_actual_format = _instance1.to_dict()["created_at"]
        _class_attr_value_get = _instance1_User.to_dict()['__class__']
        # test format inside the dictionary
        self.assertEqual(_updated_expected_format, _updated_actual_format)
        self.assertEqual(_created_expected_format, _created_actual_format)
        self.assertEqual(_class_attr_value_expected, _class_attr_value_get)


class TestBaseModelpep8(unittest.TestCase):
    """ValIdate pep8"""

    def test_pep8(self):
        """Test For Base File And Test_base File pep8"""
        _style = pep8.StyleGuide(quiet=True)
        _base_mod = "models/base_model.py"
        _test_base_mod = "tests/test_models/test_base_model.py"
        _result = _style.check_files([_base_mod, _test_base_mod])
        self.assertEqual(_result.total_errors, 2)


class TestDocsBaseModel(unittest.TestCase):
    """Test Docstrings For Base And test_base Files"""

    def test_module(self):
        """Check Module Docstrings"""
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class(self):
        """Check Class Docstrings"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method(self):
        """Check Method Docstrings"""
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
