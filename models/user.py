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
    email = ''
    password = ''
    first_name = ''
    last_name = ''
