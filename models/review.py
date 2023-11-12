#!/usr/bin/python3
"""this is the class(blueprint)"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class
    this involves public class attributes of
    - place_id
    - user_id
    - text
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ''
        self.user_id = ''
        self.text = ''
