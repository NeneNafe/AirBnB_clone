#!/usr/bin/python3
"""this is a class(blueprint)"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """this is the amenity class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ''
