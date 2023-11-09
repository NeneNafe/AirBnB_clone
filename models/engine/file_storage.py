#!/usr/bin/python3

import json
import os
"""Define a class"""


class FileStorage:
    """
    a class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instance
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dict objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(file=FileStorage.__file_path, mode='w') as file:
            serializeddata = json.dumps(FileStorage.__objects)
            file.write(serializeddata)

    def reload(self):
        """deserialization of the object file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(file=FileStorage.__file_path, mode='r') as file:
                deserializeddata = json.load(file)
                FileStorage.__objects = deserializeddata
        else:
            pass
