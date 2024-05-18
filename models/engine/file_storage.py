#!/usr/bin/python3
"""Module That Contain FileStorage Class"""

import json
import os.path
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage():
    """
    FileStorage Class That Performs Actions
    Within Objects Created And json File
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All Method Returns The __Objects Dictionary"""
        return FileStorage.__objects

    def new(self, _obj):
        """
        New Method Update __Objects Dictionary
        Each Time That A New Object Is Created
        """
        if _obj:
            _key = type(_obj).__name__ + "." + _obj.id
            FileStorage.__objects[_key] = _obj

    def save(self):
        """
        Save Method That Saves All Objects Inside A File In JSON Represetation
        """
        _d = {}
        for _key, _obj in FileStorage.__objects.items():
            _d[_key] = _obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_f:
            json.dump(_d, json_f)

    def reload(self):
        """
        Reload Method That Update __Objects Dictionary From JSON File
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as js_f:
                for _key, _obj in json.loads(js_f.read()).items():
                    _obj = eval(_obj['__class__'])(**_obj)
                    FileStorage.__objects[_key] = _obj
