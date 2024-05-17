#!/usr/bin/python3
"""Unittest for basemodel file: class and methods"""

import pep8
import unittest
import os
from models import base_model
from models.base_model import BaseModel
from datetime import datetime


class Test_Base_Model_outputs(unittest.TestCase):
    """Test_Base_outputs test for Base class"""

    def test_unique_id(self):
        """
        test_unique_id method that test if id is unique
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.unique_id, instance2.unique_id)

    def test_id_type(self):
        """
        test_id_type method that test if type of id is correct
        """
        instance1 = BaseModel()
        self.assertEqual('<class \'str\'>', str(type(instance1.unique_id)))

    def test_exec_file(self):
        """
        test_exec_file method to test if file has read, write and exec
        permissions
        """
        read = os.access('models/base_model.py', os.R_OK)
        self.assertEqual(True, read)
        write = os.access('models/base_model.py', os.W_OK)
        self.assertEqual(True, write)
        exec = os.access('models/base_model.py', os.X_OK)
        self.assertEqual(True, exec)

    def test_save(self):
        """
        test_save method to test if each time that the instance is
        saved the update_at attribute is updated
        """
        instance1 = BaseModel()
        attr_updated_before_save = instance1.update_time
        instance1.save()
        attr_updated_after_save = instance1.update_time
        self.assertNotEqual(attr_updated_before_save, attr_updated_after_save)

    def test_to_dict(self):
        """
        test_to_dict method that test if a dictionary is returned
        and if updated_at and creation_time attributes are in the correct
        format
        """
        instance1 = BaseModel()
        # test type of return
        self.assertEqual('<class \'dict\'>', str(type(instance1.to_dict())))

        updated_expected_format = instance1.update_time.isoformat()
        created_expected_format = instance1.creation_time.isoformat()
        class_attr_value_expected = type(instance1).__name__
        updated_actual_format = instance1.to_dict()["update_time"]
        created_actual_format = instance1.to_dict()["creation_time"]
        class_attr_value_get = instance1.to_dict()['class_name']
        # test format inside the dictionary
        self.assertEqual(updated_expected_format, updated_actual_format)
        self.assertEqual(created_expected_format, created_actual_format)
        self.assertEqual(class_attr_value_expected, class_attr_value_get)


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        base_mod = "models/base_model.py"
        test_base_mod = "tests/test_models/test_base_model.py"
        result = style.check_files([base_mod, test_base_mod])
        self.assertEqual(result.total_errors, 0)


class TestDocsBaseModel(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(BaseModel):
            self.assertTrue(len(getattr(BaseModel, func).__doc__) > 0)


if __name__ == "__main__":
    unittest.main()

