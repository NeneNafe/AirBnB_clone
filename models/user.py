#!/usr/bin/python3
"""this is a class"""
from models.base_model import BaseModel


class User(BaseModel):
    """this is a user class that inherits from BaseModel class"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    