#!/usr/bin/python3
"""define Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City inheriting from BaseModel
    public class attributes
    - state_id
    - name
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ''
        self.name = ''
