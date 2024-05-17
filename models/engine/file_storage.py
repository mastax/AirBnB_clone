#!/usr/bin/python3

import json
import os

class FileStorege:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

def all(self):
    """Returns the dixtionary __objects."""
    return self.__objects

def new(self, obj):
    """Returns the dictionary __objects."""
    key = "{}.{}".format(obj.__class__.__name__, obj.id)
    self.__objects[key] = obj

def save(self):
    """Serializes __objects to the JSON file (path: __file_path)."""
    data = {}
    for key, obj in self.__objects.items():
        data[key] = obj.to_dict()

    with open(self.__file_path,"w") as file:
        json.dump(data, file)
    
def reload(self):
    """Deserializes the JSON file to __objects."""
    if os.path.exists(self.__file_path):
        with open(self.__file_path, "r") as file:
            data = json.load(file)
            for key, value in data.items():
                class_name, obj_id = key.split(".")
                module_name = "models." + class_name
                module = __import__(module_name, fromlist=[class_name])
                cls = getattr(module, class_name)
                self.__object[key] = cls(**value)