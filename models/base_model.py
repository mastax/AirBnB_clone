#!/usr/bin/python3
"""This File Contain The Parent Class BaseModel"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """BaseModel Class Parent"""
    def __init__(self, *args, **kwargs):
        """
        __init__ Constructor Method Of The Class
        """
        if kwargs != {}:
            for _key, _value in kwargs.items():
                if _key == "created_at" or _key == "updated_at":
                    _val = datetime.strptime(_value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, _key, _val)
                    continue
                if _key != "__class__":
                    setattr(self, _key, _value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """__str__ Method That RString Representation Of The Instance
        Returns:
        [str]: Instance Of BaseModel String Representation"""
        s = "[{:s}] ({:s}) {}"
        return s.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Save Method That Saves Instance Information In JSON File
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict Method That Return Dictionary Representation Of The Instance

        Returns:
            [dict]: Dictionary With Information About The BaseModel Instance
        """
        _new = dict(self.__dict__)
        _new["__class__"] = type(self).__name__
        _new["created_at"] = _new["created_at"].isoformat()
        _new["updated_at"] = _new["updated_at"].isoformat()

        return _new