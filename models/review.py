#!/usr/bin/python3
"""this is the class(blueprint)"""
from base_model import BaseModel


class Review(BaseModel):
    """Review class
    this involves public class attributes of
    - place_id
    - user_id
    - text
    """
    place_id = ''
    user_id = ''
    text = ''
