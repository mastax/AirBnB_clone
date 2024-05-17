#!/usr/bin/python3
"""This File Contain The Parent Class BaseModel"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """The BaseModel Class"""
    def __init__(self):
        """Initialize attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Retunr String Reprisentation."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update Update_time attribute with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary reprisentation."""
        data = self.__dict__.copy()
        data['class_name'] = self.__class__.__name__
        data['creation_time'] = self.created_at.isoformat()
        data['update_time'] = self.updated_at.isoformat()
        return data
