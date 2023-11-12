#!/usr/bin/python3
"""this is a class"""
from models.base_model import BaseModel


class User(BaseModel):
    """this is a user class that inherits from BaseModel class
    public class attributes of
    - email
    - password
    - first_name
    - last_name
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
