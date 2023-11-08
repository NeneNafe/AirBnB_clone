#!/usr/bin/python3

import json
"""Degine a class"""


class FileStorage:
    """a class FileStorage that serializes instances to a JSON file 
    and deserializes JSON file to instance """
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """return the dict objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{<obj.__class__.__name.__}.{obj.id}"
        FileStorage.__objects[key] = obj
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        